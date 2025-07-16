# HiveBox 🐝

[![Phase](https://img.shields.io/badge/Phase-2%20(Start)-green)](https://devopsroadmap.io/projects/hivebox/)
[![Version](https://img.shields.io/badge/Version-v0.0.1-green)](https://github.com/abdo/HiveBox)
[![License](https://img.shields.io/badge/License-Educational-orange)](LICENSE)

A DevOps end-to-end hands-on project that builds a scalable RESTful API to track environmental sensor data from [openSenseMap](https://opensensemap.org/). This project follows the complete Software Development Life Cycle (SDLC) covering planning, coding, containers, testing, CI/CD, and infrastructure.

![HiveBox Architecture](https://devopsroadmap.io/projects/hivebox/img/hivebox-architecture-phase-2.png)

## 🙏 Acknowledgments

Special thanks to **[Eng. Ahmed AbouZaid](https://github.com/aabouzaid)** for proposing the HiveBox project idea and creating the comprehensive [DevOps Roadmap](https://devopsroadmap.io/projects/hivebox/). Their vision and thoughtful design helped shape this meaningful learning experience.

## 📋 Project Overview

HiveBox is designed around helping beekeepers track environmental data that affects their hives. The system fetches data from openSenseMap sensors and provides a RESTful API for monitoring temperature, humidity, and other environmental factors.

> *"Almost everyone loves honey, and we at DevOps Hive love it too and appreciate bees' role for the planet! Because bees are essential to people and the planet."* - DevOps Roadmap

**Key Learning Areas:**
- Software Production & Agile Planning
- Code & Programming (Python/Flask)
- Docker Containers & Kubernetes
- CI/CD Pipelines & Automation
- Infrastructure as Code
- Monitoring & Observability

## 🚀 Current Status

### ✅ Phase 1: Basics - DevOps Core (Completed)
- [x] Project kickoff and methodology selection (Kanban)
- [x] Git repository setup and GitHub connection
- [x] Basic application with version printing (v0.0.1)
- [x] Docker containerization
- [x] SenseBox IDs configuration
- [x] Local testing and validation
- [x] Documentation and project structure

### 🔄 Phase 2: Start - Laying the Base (Current Phase)
- [ ] Flask/FastAPI implementation
- [ ] `/version` endpoint
- [ ] `/temperature` endpoint with openSenseMap integration
- [ ] Unit tests for all endpoints
- [ ] GitHub Actions CI workflow
- [ ] Code linting (Pylint, Hadolint)
- [ ] Container best practices

### 📅 Upcoming Phases

![Phase Overview](https://devopsroadmap.io/projects/hivebox/img/hivebox-architecture-phase-3.png)

- **Phase 3**: Expand - Constructing a Shell (Kubernetes, metrics)
- **Phase 4**: Transform - Finishing the Structure (Redis/Valkey, MinIO)
- **Phase 5**: Optimize - Keep Improving (Production deployment)
- **Phase 6**: User-defined enhancements
- **Phase 7**: Capstone project with custom idea

## 🛠️ Tech Stack

| Category | Technology | Status |
|----------|------------|--------|
| **Backend** | Python 3.9+ | ✅ |
| **Framework** | Flask/FastAPI | 🔄 Next |
| **Containerization** | Docker | ✅ |
| **CI/CD** | GitHub Actions | 🔄 Next |
| **Testing** | Pytest | 🔄 Next |
| **Linting** | Pylint, Hadolint | 🔄 Next |
| **Orchestration** | Kubernetes | 📅 Future |
| **Caching** | Redis/Valkey | 📅 Future |
| **Storage** | MinIO | 📅 Future |

## 🏗️ Project Structure

```
HiveBox/
├── app/
│   ├── version_ids_script.py    # Phase 1: Basic version script
│   └── [API endpoints]          # Phase 2: Flask/FastAPI app
├── tests/                       # Phase 2: Unit tests
├── .github/
│   └── workflows/               # Phase 2: CI/CD workflows
├── Dockerfile                   # Phase 1: Container config
├── requirements.txt             # Phase 2: Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore rules
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Docker
- Git
- VS Code (recommended)

### Phase 1 - Current Implementation

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

### Phase 2 - Next Steps

The next implementation will include:
- RESTful API endpoints
- Integration with openSenseMap API
- Automated testing and CI/CD

## 📊 SenseBox Configuration

The application uses these pre-configured senseBox IDs from [openSenseMap](https://opensensemap.org/):
- `5eba5fbad46fb8001b799786`
- `5c21ff8f919bf8001adf2488`
- `5ade1acf223bd80019a1011c`

These IDs represent sensors close to each other for environmental data tracking.

## 🔧 Development Workflow

This project follows **Kanban methodology** with continuous delivery:

```
| To Do | In Progress | Testing | Done |
|-------|-------------|---------|------|
| Phase 2 API | Phase 2 Setup | - | Phase 1 Complete |
```

### Git Workflow
- `main` branch for stable releases
- `phase-X` branches for development
- Conventional commits: `feat:`, `fix:`, `docs:`

## 🎯 Learning Objectives

Following the DevOps Roadmap structure:
1. **Make it work** - Basic functionality first
2. **Make it right** - Clean code and proper structure  
3. **Make it fast** - Optimize performance later

Avoiding scope creep and focusing on incremental delivery.

## 📚 Learning Resources

- [DevOps Roadmap - HiveBox Project](https://devopsroadmap.io/projects/hivebox/)
- [openSenseMap API Documentation](https://docs.opensensemap.org/)
- [Flask Quickstart](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

## 🔄 Version History

- **v0.0.1** - Initial version with basic functionality and Docker support

## 📄 License

This project is for educational purposes as part of the DevOps learning journey.

---

*🐝 Happy DevOpsing! Remember: Make it work, make it right, make it fast!*