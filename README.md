# HiveBox 🐝

[![Phase](https://img.shields.io/badge/Phase-1%20(Basics)-blue)](https://devopsroadmap.io/projects/hivebox/)
[![Version](https://img.shields.io/badge/Version-v0.0.1-green)](https://github.com/abdo/HiveBox)
[![License](https://img.shields.io/badge/License-Educational-orange)](LICENSE)

A DevOps end-to-end hands-on project that builds a scalable RESTful API to track environmental sensor data from [openSenseMap](https://opensensemap.org/). This project follows the complete Software Development Life Cycle (SDLC) covering planning, coding, containers, testing, CI/CD, and infrastructure.

## 🙏 Acknowledgments

Special thanks to **[Eng. Ahmed AbouZaid](https://github.com/aabouzaid)** for proposing the HiveBox project idea and creating the comprehensive [DevOps Roadmap](https://devopsroadmap.io/projects/hivebox/). Their vision and thoughtful design helped shape this meaningful learning experience.

## 📋 Project Overview

HiveBox is designed around helping beekeepers track environmental data that affects their hives. The system fetches data from openSenseMap sensors and provides a RESTful API for monitoring temperature, humidity, and other environmental factors.

**Key Learning Areas:**
- Software Production & Agile Planning
- Code & Programming (Python/Flask)
- Docker Containers & Kubernetes
- CI/CD Pipelines & Automation
- Infrastructure as Code
- Monitoring & Observability

## 🚀 Current Status

### ✅ Phase 0: Preparation (Completed)
- [x] Project setup and Git repository initialization
- [x] GitHub repository creation and connection
- [x] Development environment setup
- [x] Project structure and documentation

### 🔄 Phase 1: Basics - DevOps Core (In Progress)
- [x] Basic application with version printing
- [x] Docker containerization
- [x] SenseBox IDs configuration
- [ ] Local testing and validation
- [ ] Documentation updates

### 📅 Upcoming Phases
- **Phase 2**: Start - Laying the Base (API endpoints, testing, CI)
- **Phase 3**: Expand - Constructing a Shell (Kubernetes, metrics)
- **Phase 4**: Transform - Finishing the Structure (Redis, MinIO, storage)
- **Phase 5**: Optimize - Keep Improving (Production deployment)

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python 3.9+ |
| **Framework** | Flask (planned) |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes (upcoming) |
| **Database** | TBD |
| **Caching** | Redis/Valkey (planned) |
| **Storage** | MinIO (planned) |

## 🏗️ Project Structure

```
HiveBox/
├── app/
│   └── version_ids_script.py    # Main application
├── Dockerfile                   # Container configuration
├── README.md                   # This file
└── .gitignore                  # Git ignore rules
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Docker
- Git

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/HiveBox.git
   cd HiveBox
   ```

2. **Run locally:**
   ```bash
   python3 app/version_ids_script.py
   ```

3. **Build and run with Docker:**
   ```bash
   docker build -t hivebox:0.0.1 .
   docker run hivebox:0.0.1
   ```

**Expected Output:**
```
HiveBox v0.0.1
```

## 📊 SenseBox Configuration

The application uses these pre-configured senseBox IDs from openSenseMap:
- `5eba5fbad46fb8001b799786`
- `5c21ff8f919bf8001adf2488`
- `5ade1acf223bd80019a1011c`

## 🔧 Development Workflow

This project follows **Kanban methodology** with continuous delivery:

```
| To Do | In Progress | Testing | Done |
|-------|-------------|---------|------|
| Phase 2 tasks | Phase 1 tasks | - | Phase 0 |
```

### Git Workflow
- `main` branch for stable releases
- `phase-X` branches for development
- Conventional commits: `feat:`, `fix:`, `docs:`

## 📚 Learning Resources

- [DevOps Roadmap - HiveBox Project](https://devopsroadmap.io/projects/hivebox/)
- [openSenseMap API Documentation](https://docs.opensensemap.org/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

## 🔄 Version History

- **v0.0.1** - Initial version with basic functionality

## 📄 License

This project is for educational purposes as part of the DevOps learning journey.

---

*🐝 Happy DevOpsing! Remember: Make it work, make it right, make it fast!*