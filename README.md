<div align="center">

<img src="./assets/gatito.gif" alt="Pixel cat animation" width="420" />

# CivicPulse

### Public Demographic Data Dashboard  
#### FastAPI • Docker • Chart.js • CI/CD • WCAG Accessibility

<img src="./assets/238201079-e379a33a-b428-4385-b44f-3da16e7bac9f.gif" alt="Animated star divider" width="140" />

</div>

---

## Objective

<img align="right" src="./assets/238200838-76036311-c8ea-4247-8bf8-a7077623036c.gif" alt="Seal animation" width="120" />

The CivicPulse project aimed to establish a controlled development environment for ingesting, processing, and visualizing real-world public demographic data. The primary focus was to build a secure, containerized dashboard that fetches data from the U.S. Census Bureau ACS 5-Year API, caches the results in memory via a custom Time-To-Live (TTL) service, and displays demographic telemetry using dynamic visualization tools. This practical experience was designed to deepen understanding of API service integration, accessibility compliance (WCAG), containerized deployments, and continuous integration workflows.

<br clear="right" />

---

### Skills Learned

<img src="./assets/gatito.gif" alt="Pixel cat animation" width="180" align="right" />

- Integration of government-level public web APIs with custom asynchronous client implementations.
- Design of highly accessible frontend interfaces adhering to WCAG 2.1 AA guidelines (using skip links, semantic landmarks, and ARIA live regions).
- Implementation of high-efficiency caching strategies using in-memory TTL layers.
- Application of Docker containerization and orchestration for standardizing local and production deployments.
- Configuration of robust CI/CD pipelines including testing, static analysis security testing (SAST), and secret scanning.

<br clear="right" />

---

### Tools Used

<img src="./assets/238201079-e379a33a-b428-4385-b44f-3da16e7bac9f.gif" alt="Animated star" width="110" align="right" />

- FastAPI for building high-performance asynchronous RESTful service endpoints.
- Chart.js for compiling and rendering interactive comparative graphs of population and income.
- Docker & Docker Compose for building reliable container configurations.
- GitHub Actions and GitLab CI for automating test execution, syntax checks, and security audits.
- pytest and HTTPX for mock-based testing of asynchronous services.

<br clear="right" />

---

## Steps

<div align="center">

<img src="./assets/238200838-76036311-c8ea-4247-8bf8-a7077623036c.gif" alt="Seal animation" width="90" />
<img src="./assets/238201079-e379a33a-b428-4385-b44f-3da16e7bac9f.gif" alt="Animated star" width="90" />
<img src="./assets/238200838-76036311-c8ea-4247-8bf8-a7077623036c.gif" alt="Seal animation" width="90" />

</div>

---

### 1. Environment Setup & Configuration

Create the local configuration using the provided environment template:

```bash
cp .env.example .env
```

Configure local variables including Census API keys and port allocations.

> **Ref 1:** Local Environment Configuration

---

### 2. Containerized Orchestration

Spin up the service containers to orchestrate the backend and web server setup:

```bash
docker compose up --build
```

> **Ref 2:** Container Initialization and FastAPI Server Logs

---

### 3. API Integration and In-Memory Caching

<img src="./assets/gatito.gif" alt="Pixel cat animation" width="160" align="right" />

The service layer fetches demographic telemetry from the U.S. Census Bureau ACS 5-Year API and caches datasets locally with a strict TTL boundary to avoid rate limits.

> **Ref 3:** State-Level Census Ingestion API Response

<br clear="right" />

---

### 4. Interactive Data Visualization

<img src="./assets/238201079-e379a33a-b428-4385-b44f-3da16e7bac9f.gif" alt="Animated star" width="120" align="right" />

The UI uses Chart.js to render state comparisons for population distribution and median household income while populating WCAG-compliant tabular components.

> **Ref 4:** CivicPulse Main Dashboard UI

<br clear="right" />

---

### 5. Automated CI/CD Pipelines

<img src="./assets/238200838-76036311-c8ea-4247-8bf8-a7077623036c.gif" alt="Seal animation" width="120" align="right" />

Validating code linting, unit tests with pytest, and Docker builds on every push to main.

> **Ref 5:** GitHub Actions Continuous Integration Status

<br clear="right" />

---

<div align="center">

<img src="./assets/hacker.gif" alt="Computer Typing hehe" width="260" />

### Built for secure public-data telemetry, accessibility-first design, and reproducible deployment.

</div>
