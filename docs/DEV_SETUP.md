# Developer Setup

This guide helps you get the project running locally.

## Prerequisites

- .NET SDK 9.x (builds net9 projects and can build net8 Aspire projects)
- Docker Desktop (for the Python GraphRAG container)
- VS Code or Visual Studio 2022 with .NET support

Optional:
- Dev Containers extension for VS Code

## Devcontainer

The `.devcontainer` folder contains a ready-to-use containerized dev environment. Open the repo in VS Code and choose "Reopen in Container".

## Build and Test

From the repo root:
- `dotnet restore AdvancedMemory.sln`
- `dotnet build AdvancedMemory.sln -c Debug`
- `dotnet test AdvancedMemory.sln -c Debug`

## Run the App

Option A: .NET Aspire AppHost
- Open `src/AdvancedMemory.AppHost/AdvancedMemory.AppHost.AppHost` and run the app (F5 or `dotnet run`).

Option B: Docker Compose
- Copy `.env.example` to `.env` and adjust values.
- Run `docker compose up --build` from the repo root.

## Configuration

- Use `.env` to set environment variables.
- Copy `appsettings.Development.json.example` to the appropriate project locations if you need local overrides.

## Troubleshooting

- If you see SDK version mismatches, verify your installed .NET SDKs (`dotnet --info`).
- For Docker issues, ensure Docker Desktop is running and you have adequate resources allocated.# Developer Setup

This guide helps you get the project running locally.

## Prerequisites

- .NET SDK 9.x (builds net9 projects and can build net8 Aspire projects)
- Docker Desktop (for the Python GraphRAG container)
- VS Code or Visual Studio 2022 with .NET support

Optional:
- Dev Containers extension for VS Code

## Devcontainer

The `.devcontainer` folder contains a ready-to-use containerized dev environment. Open the repo in VS Code and choose "Reopen in Container".

## Build and Test

From the repo root:
- `dotnet restore AdvancedMemory.sln`
- `dotnet build AdvancedMemory.sln -c Debug`
- `dotnet test AdvancedMemory.sln -c Debug`

## Run the App

Option A: .NET Aspire AppHost
- Open `src/AdvancedMemory.AppHost/AdvancedMemory.AppHost.AppHost` and run the app (F5 or `dotnet run`).

Option B: Docker Compose
- Copy `.env.example` to `.env` and adjust values.
- Run `docker compose up --build` from the repo root.

## Configuration

- Use `.env` to set environment variables.
- Copy `appsettings.Development.json.example` to the appropriate project locations if you need local overrides.

## Troubleshooting

- If you see SDK version mismatches, verify your installed .NET SDKs (`dotnet --info`).
- For Docker issues, ensure Docker Desktop is running and you have adequate resources allocated.