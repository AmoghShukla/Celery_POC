# ⚡ Celery_POC – Asynchronous Task Processing System

**Celery_POC** is a Proof of Concept project demonstrating how to implement **asynchronous background task processing** using Celery with Redis as a message broker.

It showcases how modern backend systems handle **long-running and non-blocking operations** efficiently using distributed task queues.

---

## Core Highlights

* **Asynchronous Task Execution**
  Offloads heavy operations to background workers

* **Redis-Based Message Broker**
  Tasks are queued and distributed reliably

* **Celery Worker System**
  Dedicated workers process tasks independently

* **Decoupled Architecture**
  API layer and execution layer are separated

* **Scalable Design**
  Supports horizontal scaling with multiple workers

---

## System Design Philosophy

Celery_POC is built around **distributed task processing**, not synchronous execution.

Traditional systems:

* Execute tasks during request-response
* Block user interaction

Celery-based systems:

* Queue tasks asynchronously
* Process tasks via workers
* Improve responsiveness and scalability

This POC reflects how real systems handle:

* Email sending
* File processing
* Background jobs
* Scheduled tasks

---

## Architecture Overview

```
Client → API → Redis Queue → Celery Worker → Result Backend
```

### Flow Explanation

1. Client sends request
2. API pushes task to Redis queue
3. Celery worker picks task
4. Task executes asynchronously
5. Result is stored or returned

---

## Project Structure

```
Celery_POC/
├── src/
│   ├── tasks/          # Celery task definitions
│   ├── worker/         # Worker configuration
│   ├── config/         # Celery & Redis setup
│   ├── routes/         # API endpoints
│   ├── services/       # Business logic
│   └── utils/          # Helper utilities
│
├── main.py             # Entry point
├── requirements.txt    # Dependencies
├── docker-compose.yml  # Redis + worker setup (if present)
└── README.md
```

---

## Key Components

| Component | Description                           |
| --------- | ------------------------------------- |
| Celery    | Task queue system                     |
| Redis     | Message broker                        |
| Worker    | Executes background jobs              |
| Task      | Unit of work processed asynchronously |
| API Layer | Accepts requests and enqueues tasks   |

---

## Business Rules Enforced

* Tasks are never executed synchronously
* All heavy operations are delegated to workers
* Queue ensures reliable task delivery
* Workers process tasks independently
* System remains responsive under load

---

## Features

* Background task execution
* Queue-based processing
* Scalable worker system
* Fault-tolerant execution
* Clean separation of concerns

---

## Tech Stack

| Category         | Technology                                |
| ---------------- | ----------------------------------------- |
| Backend          | Python                                    |
| Task Queue       | Celery                                    |
| Message Broker   | Redis                                     |
| API Framework    | FastAPI / Flask (based on implementation) |
| Containerization | Docker (optional)                         |

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AmoghShukla/Celery_POC.git
cd Celery_POC
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Start Redis Server

```bash
redis-server
```

---

### 5. Run Celery Worker

```bash
celery -A src.worker worker --loglevel=info
```

---

### 6. Run Application

```bash
python main.py
```

---

## Example Workflow

1. Client sends request
2. API enqueues task
3. Redis stores task in queue
4. Worker processes task
5. Result is returned or stored

---

## Future Enhancements

* Task result tracking (backend storage)
* Retry mechanisms for failed tasks
* Scheduled tasks using Celery Beat
* Monitoring with Flower
* Distributed multi-node workers

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is open source and available under the **MIT License**.

---

## Final Note

Celery_POC is not just about background jobs —

it is about **building scalable, non-blocking backend systems that can handle real-world workloads efficiently**.
