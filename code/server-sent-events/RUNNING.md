# Run the server-sent events sample

This ASP.NET Core sample streams updates from an HTTP endpoint.

[Read the issue](https://newsletter.francofernando.com/p/server-sent-event).

The original sample targets .NET 7, which is no longer supported. It needs the .NET 7 SDK and runtime, or a separately reviewed upgrade to a supported .NET version. No Python dependencies are required.

From this folder:

```sh
dotnet restore DemoWebApplicationSSE.sln
dotnet run --project src/DemoWebApiSSE.csproj --urls http://localhost:5000
```

In a second terminal, inspect the event stream:

```sh
curl -N http://localhost:5000/sse
```

The original browser client is in `src/View/Client.html`. Its endpoint must use the same host and port as the running server. Stop the server with Ctrl+C.

[The Polymathic Engineer](https://newsletter.francofernando.com) | [Subscribe](https://newsletter.francofernando.com/subscribe)