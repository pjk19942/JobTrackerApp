# Job Tracker App

## Overview
The **Job Tracker App** is a Python-based desktop application that helps users manage and track their job applications efficiently. It provides an intuitive interface to store job details, update statuses, log application dates, and maintain additional notes. The app integrates seamlessly with Excel for data storage, making it easy to organize and review job applications. I used ai to make it for my convenience but feel free to use it :-)

## Features
- **Add Job Listings**: Enter job details manually or fetch them from a URL.
- **Update Job Status**: Track progress with statuses like `Initial Call`, `HM Call`, `Tech Interview`, and `Offer`.
- **Log Application Dates**: Mark when you applied for a position.
- **Add Comments**: Store additional notes about each job.
- **Open Job Links**: Quickly access job postings by double-clicking the entry.
- **Excel Integration**: Automatically saves all job details for easy review and export.

## Technologies Used
- **Python** (Application logic)
- **Tkinter & ttkbootstrap** (User Interface)
- **Pandas** (Data handling and storage)
- **Requests & BeautifulSoup** (Extracting job details from URLs)
- **Excel (.xlsx) Support** (Persistent data storage)

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/pjk19942/JobTrackerApp.git
   cd job-tracker-app
   ```
2. **Install dependencies**:
   ```sh
   pip install pandas requests beautifulsoup4 ttkbootstrap openpyxl
   ```
3. **Run the application**:
   ```sh
   python JobTrackerApp.py
   ```

## Usage
1. **Add a Job**: Paste a job link and click `Add Job`.
2. **Update Job Status**: Select a job from the table and choose a new status.
3. **Mark as Applied**: Log the application date.
4. **Add Comments**: Store additional notes.
5. **Open Excel File**: Click `Open Excel Sheet` to view all data.


## Contribution
Contributions are welcome! Feel free to fork the repository, create pull requests, or report issues.

## License
This project is open-source and available under the **MIT License**.
