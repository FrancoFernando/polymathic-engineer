import tempfile
import unittest
from pathlib import Path

import yaml

import generate


class GenerateTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "code" / "bloom-filter").mkdir(parents=True)
        self.issues = [{
            "title": "Bloom [filters]", "url": generate.NEWSLETTER + "/p/bloom-filters-explained",
            "year": 2026, "topics": ["System Design", "Algorithms & Data Structures"],
            "code": "bloom-filter",
        }]
        self.write_issues()

    def write_issues(self):
        (self.root / "issues.yml").write_text(yaml.safe_dump(self.issues), encoding="utf-8")

    def snapshot(self):
        return {path.relative_to(self.root): path.read_bytes() for path in self.root.rglob("*.md")}

    def test_idempotent_and_multitopic(self):
        generate.generate(self.root)
        first = self.snapshot()
        generate.generate(self.root)
        self.assertEqual(first, self.snapshot())
        readme = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertEqual(readme.count(self.issues[0]["url"]), 2)
        self.assertIn("Bloom \\[filters\\]", readme)
        self.assertEqual(readme.count("code/bloom-filter/"), 2)

    def test_handwritten_readme_only_gets_issue_link(self):
        path = self.root / "code" / "bloom-filter" / "README.md"
        original = "# Hand-written\n\nKeep this setup command.\n"
        path.write_text(original, encoding="utf-8")
        generate.generate(self.root)
        expected = original + f"\n\n[Read the newsletter issue: {self.issues[0]['title']}]({self.issues[0]['url']}).\n"
        self.assertEqual(path.read_text(encoding="utf-8"), expected)
        generate.generate(self.root)
        self.assertEqual(path.read_text(encoding="utf-8"), expected)

    def test_existing_issue_link_is_untouched(self):
        path = self.root / "code" / "bloom-filter" / "README.md"
        original = "# Hand-written\n\n" + self.issues[0]["url"]
        path.write_text(original, encoding="utf-8")
        generate.generate(self.root)
        self.assertEqual(path.read_text(encoding="utf-8"), original)

    def test_generated_title_follows_metadata(self):
        generate.generate(self.root)
        self.issues[0]["title"] = "New title"
        self.write_issues()
        generate.generate(self.root)
        self.assertIn("# New title", (self.root / "code" / "bloom-filter" / "README.md").read_text(encoding="utf-8"))

    def test_bad_metadata_fails_without_writing(self):
        cases = ({"topics": []}, {"topics": ["Unknown"]}, {"topics": ["More", "System Design"]},
                 {"code": "../escape"}, {"code": "missing"}, {"year": True},
                 {"url": "https://example.com/p/issue"}, {"title": ""})
        for replacement in cases:
            with self.subTest(replacement=replacement):
                self.issues = [dict(self.issues[0], **replacement)]
                self.write_issues()
                before = self.snapshot()
                with self.assertRaises(ValueError):
                    generate.generate(self.root)
                self.assertEqual(before, self.snapshot())
                self.setUp_issue()

    def setUp_issue(self):
        self.issues = [{"title": "Bloom filters", "url": generate.NEWSLETTER + "/p/bloom-filters-explained",
                        "year": 2026, "topics": ["System Design"], "code": "bloom-filter"}]

    def test_duplicate_urls_rejected(self):
        self.issues.append(dict(self.issues[0]))
        self.write_issues()
        with self.assertRaisesRegex(ValueError, "Duplicate issue URL"):
            generate.generate(self.root)

    def write_paths(self, issues):
        paths = [{"title": "Start", "description": "Read these in order.", "issues": issues}]
        (self.root / "paths.yml").write_text(yaml.safe_dump(paths), encoding="utf-8")

    def test_paths_keep_their_own_order(self):
        self.issues.append({"title": "Earlier", "url": generate.NEWSLETTER + "/p/earlier",
                            "year": 2025, "topics": ["System Design"]})
        self.write_issues()
        self.write_paths(["earlier", "bloom-filters-explained"])
        generate.generate(self.root)
        first = self.snapshot()
        generate.generate(self.root)
        self.assertEqual(first, self.snapshot())
        readme = (self.root / "README.md").read_text(encoding="utf-8")
        section = readme[readme.index("## Reading Paths"):readme.index("## Issues")]
        self.assertIn(f"1. [Earlier]({self.issues[1]['url']})", section)
        self.assertIn(f"2. [Bloom \\[filters\\]]({self.issues[0]['url']}) ([code](code/bloom-filter/))", section)

    def test_bad_paths_fail_without_writing(self):
        for issues in ([], ["missing"], ["bloom-filters-explained", "bloom-filters-explained"]):
            with self.subTest(issues=issues):
                self.write_paths(issues)
                before = self.snapshot()
                with self.assertRaises(ValueError):
                    generate.generate(self.root)
                self.assertEqual(before, self.snapshot())

    def test_order_is_preserved(self):
        self.issues.append({"title": "Earlier", "url": generate.NEWSLETTER + "/p/earlier",
                            "year": 2025, "topics": ["System Design"]})
        self.write_issues()
        generate.generate(self.root)
        readme = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertLess(readme.index(self.issues[0]["url"]), readme.index(self.issues[1]["url"]))


if __name__ == "__main__":
    unittest.main()