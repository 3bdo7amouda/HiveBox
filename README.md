# HiveBox 🐝

[![Phase](https://img.shields.io/badge/Phase-2%20(Completed)-green)](https://devopsroadmap.io/projects/hivebox/)
[![Version](https://img.shields.io/badge/Version-v0.1.2-green)](https://github.com/abdo/HiveBox)
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
- [x] Docker containerization with basic setup
- [x] SenseBox IDs configuration
- [x] Local testing and validation
- [x] Documentation and project structure

### 🔄 Phase 2: Start - Laying the Base (Completed)
- [x] Flask implementation with full REST API
- [x] `/` endpoint (API discovery)
- [x] `/version` endpoint (health check)
- [x] `/temperature` endpoint with openSenseMap integration
- [x] Advanced error handling and input validation
- [x] Unit tests for all endpoints with mocking
- [x] Docker best practices implementation
- [x] Production-ready containerization
- [x] GitHub Actions CI workflow
- [x] Code linting integration (Pylint, Hadolint)
- [x] Automated testing in CI pipeline

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
| **Backend** | Python 3.12 | ✅ |
| **Framework** | Flask | ✅ |
| **API Integration** | openSenseMap REST API | ✅ |
| **Containerization** | Docker (Multi-layer, Security) | ✅ |
| **Testing** | Pytest with Mocking | ✅ |
| **CI/CD** | GitHub Actions | ✅ |
| **Linting** | Pylint, Hadolint | ✅ |
| **Orchestration** | Kubernetes | 📅 Future |
| **Caching** | Redis/Valkey | 📅 Future |
| **Storage** | MinIO | 📅 Future |

## 🏗️ Project Structure

```
HiveBox/
├── app/
│   └── main.py                  # ✅ Flask REST API with full functionality
├── tests/
│   ├── __init__.py             # ✅ Test package
│   └── test_main.py            # ✅ Comprehensive unit tests
├── .github/
│   └── workflows/              # ✅ CI/CD workflows
├── Dockerfile                  # ✅ Production-ready container
├── .dockerignore               # ✅ Optimized build context
├── requirements.txt            # ✅ Pinned dependencies
├── README.md                   # ✅ Project documentation
└── .gitignore                  # ✅ Git ignore rules
```

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Docker
- Git

### Current Implementation (Phase 2)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/HiveBox.git
   cd HiveBox
   ```

2. **Run locally:**
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Run Flask app
   export FLASK_APP=app/main.py
   flask run
   ```

3. **Run with Docker:**
   ```bash
   # Build optimized image
   docker build -t hivebox:0.1.1 .
   
   # Run container
   docker run -d -p 5000:5000 --name hivebox-app hivebox:0.1.1
   ```

4. **Test the API:**
   ```bash
   # API discovery
   curl http://localhost:5000/
   
   # Health check
   curl http://localhost:5000/version
   
   # Get temperature data
   curl http://localhost:5000/temperature
   
   # Get specific sensor
   curl "http://localhost:5000/temperature?sensebox_id=5eba5fbad46fb8001b799786"
   ```

5. **Run tests:**
   ```bash
   # Run all tests
   pytest
   
   # Run with coverage
   pytest --cov=app
   ```

## 📊 API Endpoints

### Current Functionality

| Endpoint | Method | Description | Status |
|----------|--------|-------------|--------|
| `/` | GET | API discovery and welcome | ✅ |
| `/version` | GET | Health check and version info | ✅ |
| `/temperature` | GET | All sensors temperature data | ✅ |
| `/temperature?sensebox_id=ID` | GET | Specific sensor temperature | ✅ |

### Example Response
```json
{
  "timestamp": "2025-07-22T12:00:00Z",
  "total_results": 3,
  "successful_results": 2,
  "failed_results": 1,
  "data": [
    {
      "sensebox_id": "5eba5fbad46fb8001b799786",
      "status": "success",
      "name": "Environmental Station",
      "location": {
        "coordinates": [11.5820, 48.1351],
        "type": "Point"
      },
      "temperature": {
        "sensor_id": "sensor123",
        "phenomenon": "Lufttemperatur",
        "unit": "°C",
        "value": 23.4,
        "timestamp": "2025-07-22T11:45:00Z"
      }
    }
  ]
}
```

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
| GitHub Actions | CI/CD Setup | Unit Tests | Flask API |
| Code Linting | - | Docker Build | Error Handling |
```

### Git Workflow
- `main` branch for stable releases
- `phase-X` branches for development
- Conventional commits: `feat:`, `fix:`, `docs:`

## 🎯 Learning Objectives

Following the DevOps Roadmap structure:
1. **Make it work** - ✅ Basic functionality complete
2. **Make it right** - ✅ Clean code and proper structure implemented  
3. **Make it fast** - 🔄 CI/CD optimization in progress

## 📚 Learning Resources

- [DevOps Roadmap - HiveBox Project](https://devopsroadmap.io/projects/hivebox/)
- [openSenseMap API Documentation](https://docs.opensensemap.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## 🔄 Version History

- **v0.1.2** - Complete Flask API with openSenseMap integration, Docker optimization, comprehensive testing, GitHub Actions CI
- **v0.1.1** - Initial version with basic functionality

## 📄 License

This project is for educational purposes as part of the DevOps learning journey.

---