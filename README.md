# Advanced Memory (Sparrow23)

Polyglot memory services scaffold built with .NET 9 + .NET Aspire and a companion Python GraphRAG service. This repo was initialized via the "project-setup" dynamic workflow, with planning artifacts, milestones, and issue templates already in place.

## What’s here

- docs/
	- Advanced Memory .NET - Dev Plan.md (planning doc)
	- index.html (interactive report)
- src/
	- AdvancedMemory.sln (solution)
	- AdvancedMemory.Api (ASP.NET Core Web API)
	- AdvancedMemory.Core, AdvancedMemory.Shared (class libraries)
	- AdvancedMemory.AppHost (Aspire Starter: AppHost, ServiceDefaults, ApiService, Web)
- services/
	- GraphRagService (FastAPI placeholder with Dockerfile)
- docker-compose.yml (local orchestration for ApiService + GraphRagService)
- appsettings.Development.json.example and .env.example (configuration templates)
- .github/
	- ISSUE_TEMPLATE/ (Application Plan + Epic templates)
	- workflows/ (existing repo setup workflows)

## Quick start

Prereqs:
- .NET SDK 9.x installed (SDK can build net8 Aspire projects as well)
- Docker Desktop (for GraphRag service container)

Build and test:
- From repo root: run dotnet restore, dotnet build, and dotnet test for the solution `AdvancedMemory.sln`.

Run locally (option A: .NET Aspire AppHost):
- Start the Aspire AppHost project in `src/AdvancedMemory.AppHost/AdvancedMemory.AppHost.AppHost` (F5 from VS/VS Code or `dotnet run`).

Run locally (option B: compose):
- Copy `.env.example` to `.env` and adjust values.
- `docker compose up --build` to run the GraphRag service alongside the API.

## Developer setup

- See `docs/DEV_SETUP.md` for environment setup, devcontainer usage, and local run instructions.
- See `.env.example` and `appsettings.Development.json.example` for config shape.

## CI

- Sample GitHub Actions workflow is provided at `docs/ci/dotnet-ci.yml`. Move it to `.github/workflows/` in your fork with a token that has `workflow` scope to enable.

## Planning and tracking

- Application Plan issue: created using the included template.
- Epics: one per phase, mapped to milestones.
- GitHub Project: https://github.com/users/nam20485/projects/19

## License

See `LICENSE.md`.
