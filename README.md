# Job Matching System

![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

The Job Matching System is a Flask-based backend for a job matching platform. It allows job seekers to create profiles, apply for job postings, and be associated with skill sets. Employers can post job listings, review applications, and specify required skill sets. The system uses MongoDB as the database for storing information about job seekers, job postings, applications, and skill sets.

## Features

- **Job Seekers:**
  - Create and manage job seeker profiles.
  - Retrieve details of a specific job seeker.
  - Update and delete job seeker profiles.

- **Job Postings:**
  - Post and manage job listings.
  - Retrieve details of a specific job posting.
  - Update and delete job postings.

- **Applications:**
  - Submit and manage job applications.
  - Retrieve details of a specific application.
  - Update and delete applications.

- **Skill Sets:**
  - Create and manage skill sets.
  - Retrieve details of a specific skill set.
  - Update and delete skill sets.

- **Additional Features:**
  - Apply for a job posting.
  - Add a skill set to a job posting.

## Entity-Relationship Diagram (ER Diagram)
<img width="663" alt="Screenshot 2023-12-01 140422" src="https://github.com/sonukumar047/job_matching_system/assets/121346782/678759e9-8035-4134-a5a2-5f6f133ac3b6">

# API Endpoints

## Job Seekers

- **GET /jobseekers:**
  - Get all job seekers.

- **POST /jobseekers:**
  - Create a new job seeker profile.

- **GET /jobseekers/<seeker_id>:**
  - Get details of a specific job seeker.

- **PUT /jobseekers/<seeker_id>:**
  - Update a specific job seeker's profile.

- **DELETE /jobseekers/<seeker_id>:**
  - Delete a specific job seeker's profile.

## Job Postings

- **GET /jobpostings:**
  - Get all job postings.

- **POST /jobpostings:**
  - Create a new job posting.

- **GET /jobpostings/<job_id>:**
  - Get details of a specific job posting.

- **PUT /jobpostings/<job_id>:**
  - Update a specific job posting.

- **DELETE /jobpostings/<job_id>:**
  - Delete a specific job posting.

## Applications

- **GET /applications:**
  - Get all job applications.

- **POST /applications:**
  - Create a new job application.

- **GET /applications/<app_id>:**
  - Get details of a specific job application.

- **PUT /applications/<app_id>:**
  - Update a specific job application.

- **DELETE /applications/<app_id>:**
  - Delete a specific job application.

## Skill Sets

- **GET /skillsets:**
  - Get all skill sets.

- **POST /skillsets:**
  - Create a new skill set.

- **GET /skillsets/<skill_set_id>:**
  - Get details of a specific skill set.

- **PUT /skillsets/<skill_set_id>:**
  - Update a specific skill set.

- **DELETE /skillsets/<skill_set_id>:**
  - Delete a specific skill set.

## Additional Features

- **POST /jobpostings/<job_id>/apply:**
  - Apply for a job posting.

- **POST /jobpostings/<job_id>/addskillset:**
  - Add a skill set to a job posting.


## Getting Started

### Prerequisites

- Python
- MongoDB

## Run the Flask Application:

- Execute python app.py to start the Flask application.
- The server will run at http://localhost:5000/ by default.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sonukumar047/job_matching_system.git
   cd job-matching-system
