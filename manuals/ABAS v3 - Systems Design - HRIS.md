# Human Resources Information System

*Systems Design*

# Revision History

| **Date** | **Version** | **Description** | **Author** |
| --- | --- | --- | --- |
| **2025-01-28** | Draft 1.0.0 | Initial Draft | Alfredo Sanchez Jr |
|  |  |  |  |
|  |  |  |  |
| **** |  |  |  |

# **1. Introduction**

## **1.1 Purpose**

This manual serves as the comprehensive guide to the design and implementation of the Human Resources Information System (HRIS) within ABAS v3. It complements the broader ABAS System Design Document by providing a focused guide specifically for HR users and stakeholders. This manual is intended to provide a clear understanding of the system's functionalities, processes, and technical specifications to all stakeholders, including:

- HR Professionals and staff who utilize the system for daily operations.
- System Administrators responsible for managing and maintaining the HRIS.
- IT personnel involved in the technical aspects of the system.
- Management and decision-makers who rely on HR data for strategic planning.

The primary focus of this manual is to equip users with the knowledge and resources necessary to effectively navigate and utilize the HRIS to streamline HR processes, improve data accuracy, and enhance overall HR efficiency within the organization.

## **1.2 Scope**

This manual specifically addresses the HR modules within the ABAS v3 system, which is an upgrade from ABAS v2.5.x. ABAS v3 utilizes CodeIgniter on the backend with RESTful APIs and React.Next on the frontend for enhanced performance and user experience. The HRIS module is the first to be implemented in this new version.

The HR modules covered in this document include:

- **Recruitment and Onboarding:** Applicant tracking, new hire onboarding, and integration with external recruitment platforms.
- **Performance Management:** Performance reviews, goal setting, feedback mechanisms, and performance reporting.
- **Compensation and Benefits:** Payroll processing, benefits administration, salary structures, and time and attendance management.
- **Employee and Manager Self-Service:** Employee and manager access to personal information, leave requests, performance reviews, and other HR-related tasks.
- **Talent Management:** Succession planning, learning and development, and career development initiatives.
- **HR Reporting and Analytics:** Standard and custom reporting capabilities for HR data analysis and decision-making.
- **Employee 201 File Management:** Maintaining comprehensive employee records, including personal information, employment history, and performance documentation.
- **Attendance and Leave Management:** Tracking employee attendance, leaves of absence (including AWOL), and time-off requests.
- **Overtime and Undertime Management:** Recording and calculating overtime and undertime hours for compensation purposes.
- **Official Business and Travel Management:** Managing requests and approvals for official business trips and travel.
- **OJT 201 File Management:** Tracking and managing on-the-job training records for employees.
- **HR Memos and Bulletins:** Disseminating important HR announcements, policies, and updates to employees.
- **Organizational Chart Management:** Maintaining an up-to-date organizational chart reflecting the company's structure and reporting relationships.
- **Crew Movements:** Managing and tracking the transfer of crew members between ships to ensure efficient crew deployment and scheduling.
- **Job Descriptions:** Creating, storing, and managing job descriptions for use in recruitment, performance management, and other HR processes.
- **Employee Offboarding and Record Retention:** Managing the offboarding process for separated, terminated, or retired employees, including recording separation/retirement details, managing exit interviews (if applicable), transferring records to an inactive status, and ensuring compliance with record retention policies.
- **Statutory Compliance:**
    - **BIR Alpha List Reporting:** Generating the annual Alphabetical List of Employees/Payees required by the BIR.
    - **SSS Loan/Leave Management:** Managing loan/leave applications and benefits in compliance with SSS regulations.
    - **PhilHealth Sick Leave Benefits:** Processing sick leave benefits claims in accordance with PhilHealth guidelines.
    - **Pag-IBIG Loan Management:** Facilitating employee applications for Pag-IBIG loans.

This manual does not cover other non-HR modules within ABAS v3.

## **1.3 Goals and Objectives**

The HRIS within ABAS v3 is designed to achieve the following key goals and objectives, aligning with the overall ABAS objectives of reliability, security, efficiency, and user-friendliness:

- **Streamline HR Processes:** Automate and optimize core HR functions to reduce manual effort and improve efficiency.
- **Enhance Data Accuracy:** Ensure the accuracy and integrity of HR data for reliable reporting and informed decision-making.
- **Empower Employees and Managers:** Provide self-service tools to employees and managers for greater autonomy and access to HR information.
- **Improve Compliance:** Facilitate adherence to relevant labor laws and regulations, including those related to BIR, SSS, PhilHealth, and Pag-IBIG.
- **Support Strategic HR:** Provide data-driven insights to support strategic HR planning and initiatives.
- **Enhance the Employee Experience:** Create a positive and user-friendly experience for employees interacting with the HRIS.

By achieving these goals, the HRIS aims to contribute to the overall success of the organization by enabling a more efficient, effective, and strategic HR function.

# **2. System Overview**

## **2.1 HRIS Architecture**

The HRIS within ABAS v3 is designed as an integrated module within the larger system architecture. It shares data and interacts with other modules, such as payroll and finance, while maintaining a distinct focus on HR functions.

ABAS v3 has been upgraded to utilize CodeIgniter on the backend with RESTful APIs and React.Next on the frontend for enhanced performance and user experience. This architecture allows for a more modular and scalable system, enabling easier maintenance and updates.

The following diagram provides a visual representation of the HRIS architecture and its key components:

*figure …*

HRIS architecture diagram adapted from ABAS System Design Document, updated to reflect CodeIgniter, RESTful APIs, and React.Next

- **Client-Side (User Interface):** This is the front-end of the HRIS, built with React.Next, where users interact with the system. It provides access to various HR functions and data through a user-friendly interface, consisting of functional and graphical components.
- **Server-Side (Logical Interface):** This is the core of the HRIS, built with CodeIgniter and implementing RESTful APIs, responsible for processing data, enforcing business rules, and managing workflows. It manages incoming and outgoing requests and interacts with the database.
- **Data Interface (Data Storage):** This is where all HR data is stored securely in a relational database. The database is designed to ensure data integrity, confidentiality, and availability.
- **External Systems:** The HRIS may integrate with external systems, such as payroll providers, benefits platforms, or recruitment agencies, to exchange data and streamline processes.

## **2.2 HR Modules**

The HRIS within ABAS v3 comprises several interconnected modules, each dedicated to specific HR functions. These modules work together to provide a comprehensive solution for managing the entire employee lifecycle.

- **Recruitment and Onboarding:** This module streamlines the hiring process, from posting job openings and tracking applicants to onboarding new hires. It includes features for:
    - **Job Description Management:** Creating, storing, and accessing accurate and up-to-date job descriptions that are used for job postings, applicant screening, and setting clear expectations during onboarding.
    - **Managing job requisitions:** Initiating and tracking recruitment requests.
    - **Applicant Tracking:** Managing applications, screening candidates, and scheduling interviews.
    - **Onboarding Automation:** Automating tasks like offer letters, background checks, and new hire paperwork.
- **Performance Management:** This module facilitates performance reviews, goal setting, and feedback processes. It provides tools for:
    - Setting performance objectives.
    - Tracking progress.
    - Conducting performance appraisals.
    - Generating performance reports.
- **Compensation and Benefits:** This module manages all aspects of employee compensation and benefits, including:
    - Payroll processing.
    - Benefits administration.
    - Salary structures.
    - Time and attendance tracking.
- **Employee and Manager Self-Service:** This module empowers employees and managers to access and manage their own HR information. Employees can:
    - Update personal details.
    - Request time off.
    - View pay stubs.
    - Access company policies.
    
    Managers can:
    
    - Approve leave requests.
    - Conduct performance reviews.
    - Access team performance data.
- **Talent Management:** This module supports talent development initiatives, such as:
    - Succession planning.
    - Learning and development programs.
    - Career development plans.
- **HR Reporting and Analytics:** This module provides comprehensive reporting and analytics capabilities for HR data. It allows HR professionals to:
    - Generate standard reports.
    - Create custom reports.
    - Analyze HR metrics.
- **Employee 201 File Management:** This module provides a centralized repository for storing and managing employee records, including:
    - **Active Employee Records:** Maintaining records for current employees.
    - **Offboarding and Record Retention:** Managing the offboarding process for separated, terminated, or retired employees, including:
        - Recording separation/retirement details.
        - Managing exit interviews (if applicable).
        - Transferring records to an inactive status.
        - Ensuring compliance with record retention policies.
- **Attendance and Leave Management:** This module tracks employee attendance, manages leave requests, and monitors absences.
- **Overtime and Undertime Management:** This module accurately records and calculates overtime and undertime hours for payroll processing and compensation purposes.
- **Official Business and Travel Management:** This module streamlines the process of requesting, approving, and tracking official business trips and travel expenses.
- **OJT 201 File Management:** This module manages on-the-job training records, ensuring that employee training progress is tracked and documented effectively.
- **HR Memos and Bulletins:** This module provides a platform for disseminating important HR announcements, policy updates, and company-wide communications to employees.
- **Organizational Chart Management:** This module maintains an up-to-date organizational chart, providing a visual representation of the company's structure, reporting relationships, and employee positions.
- **Crew Movements:** This module facilitates the efficient management and tracking of crew transfers between ships. It enables HR to plan and execute crew changes, track crew member locations, manage crew schedules, and ensure optimal crew deployment across the fleet. This module may include features such as:
    - Transfer Requests and Approvals.
    - Crew Scheduling and Rostering.
    - Travel and Logistics Management.
    - Crew Records and Documentation.

## **2.3 Reporting and Analytics**

The HRIS offers robust reporting and analytics capabilities that enable HR professionals to gain valuable insights from HR data. The system provides a variety of standard reports, including:

- **Employee Demographics:** Reports on employee age, gender, ethnicity, and other demographic characteristics.
- **Turnover Analysis:** Reports on employee turnover rates, reasons for leaving, and trends over time.
- **Performance Metrics:** Reports on performance ratings, goal attainment, and performance improvement plans.
- **Compensation Analysis:** Reports on salary ranges, pay equity, and compensation trends.
- **Benefits Utilization:** Reports on employee enrollment in benefit plans and utilization of benefit programs.

In addition to standard reports, the HRIS allows users to create custom reports based on specific criteria and data needs. The reporting and analytics tools help HR professionals to:

- Identify trends and patterns in HR data.
- Measure the effectiveness of HR programs and initiatives.
- Make informed decisions about HR policies and practices.
- Support strategic HR planning and organizational goals.

By providing comprehensive reporting and analytics capabilities, the HRIS empowers HR professionals to leverage data to drive improvements in HR processes and organizational performance.

# **3. Data Management**

## **3.1 Data Structure**

The HRIS within ABAS v3 employs a relational database structure to organize and manage HR data efficiently. This structure uses tables to store data elements and defines relationships between these tables, ensuring data integrity and consistency. The database structure may have been modified in ABAS v3 to accommodate the new technologies and HRIS functionalities.

### **Tables:**

The database comprises various tables, each dedicated to specific HR entities, such as employees, positions, departments, leave records, performance reviews, and more. Each table contains a set of fields that store relevant attributes of the entity. For example, the "Employees" table might include fields like Employee ID, Name, Address, Date of Birth, Job Title, Department, etc.

figure here

### **Relationships:**

Relationships between tables establish connections based on common fields. For instance, the "Employees" table might have a relationship with the "Departments" table based on the "Department ID" field, allowing the system to link employees to their respective departments.

figure here

### **Data Dictionary:**

A data dictionary provides detailed descriptions of each table and field within the database, including data types, formats, and any validation rules. This dictionary serves as a valuable reference for understanding the structure and meaning of HR data.

*figure here*

## **3.2 Data Security and Privacy**

Protecting sensitive HR data is a top priority. The HRIS incorporates various security measures to ensure data confidentiality, integrity, and availability:

- **Access Controls:** The system implements role-based access control (RBAC), granting users access to data and functionalities based on their roles and responsibilities. This ensures that only authorized personnel can access and modify specific HR data.
- **Data Encryption:** Sensitive data, such as employee identification numbers, salary information, and performance reviews, is encrypted both in transit and at rest. This protects data from unauthorized access even if a security breach occurs.
- **Audit Trails:** The system maintains audit trails that record all data access, modifications, and deletions. This provides a history of data changes and helps to identify any unauthorized or suspicious activity.
- **Regular Backups:** The HRIS database is regularly backed up to ensure data recovery in case of system failures or data loss incidents.
- **Data Privacy Compliance:** The system adheres to relevant data privacy regulations in the Philippines, particularly the Data Privacy Act of 2012 (Republic Act No. 10173). This Act outlines the principles of data privacy, rights of data subjects, and obligations of data controllers and processors. The HRIS ensures compliance with this Act by implementing appropriate security measures, obtaining consent for data collection and processing, and providing data subjects with access to and control over their personal information.

## **3.3 Data Integration**

- **System Integration:** The HRIS may integrate with other systems within the organization, such as payroll systems, benefits providers, or time and attendance systems. Integration allows for seamless data flow between systems, reducing data redundancy and improving data accuracy.

## **3.4 Data Quality and Maintenance**

Maintaining high-quality HR data is essential for accurate reporting, informed decision-making, and efficient HR operations. The HRIS includes features to support data quality:

- **Data Validation:** Validation rules are implemented to ensure that data entered into the system meets predefined criteria. This helps to prevent errors and maintain data consistency.
- **Data Cleansing:** Regular data cleansing activities, such as identifying and correcting duplicate records or outdated information, help to improve data accuracy.
- **Data Governance:** Establishing data governance policies and procedures helps to ensure that data is managed consistently and responsibly across the organization.

By implementing robust data management practices, the HRIS ensures that HR data is accurate, secure, and readily available to support HR operations and strategic decision-making.

# **4. User Roles and Permissions**

## **4.1 User Roles and Use Cases**

The HRIS in ABAS v3 defines various user roles, each with specific permissions and access levels to ensure data security and maintain confidentiality. Here are some of the key roles and their potential use cases across different HR modules:

### **4.2 HR Administrator**

Full access to all HR modules and data, responsible for system configuration, user management, and overall system maintenance.

- **Recruitment and Onboarding:**
    - "Configures integration with JobStreet to streamline applicant tracking."
    - Configure integration with external recruitment platforms.
    - Generate reports on recruitment metrics (time-to-hire, cost-per-hire, etc.).
    - Manage user access and permissions for the recruitment module.
    - Set up automated onboarding workflows (e.g., new hire notifications, document distribution).
- **Performance Management:**
    - "Defines a new performance review template with updated rating scales."
    - Define performance review cycles and templates.
    - Configure performance rating scales and weighting.
    - Generate performance reports for analysis and decision-making.
    - Manage user access and permissions for the performance management module.
- **Compensation and Benefits:**
    - "Adds a new health insurance plan to the employee benefits enrollment options."
    - Configure pay grades, salary structures, and compensation rules.
    - Manage benefits enrollment periods and options.
    - Generate payroll reports and analyze compensation trends.
    - Manage user access and permissions for the compensation and benefits module.
- **Employee 201 File Management:**
    - "Creates a new employee record with complete personal and employment details."
    - Create and manage employee records, including personal information, employment history, and performance documentation.
    - Configure document templates for employee files.
    - Manage user access and permissions for employee files.
    - Ensure compliance with data privacy regulations for employee data.
- **Attendance and Leave Management:**
    - "Updates the company's holiday calendar for the upcoming year."
    - "Configures a new type of leave for paternity leave, setting the accrual rate and eligibility criteria."
    - "Creates and manages the company holiday table, ensuring it includes both national and company-specific holidays."
    - Configure leave policies, accrual rates, and eligibility criteria.
    - Manage holiday calendars and working days.
    - Generate attendance reports and analyze leave trends.
    - Manage user access and permissions for attendance and leave data.
- **Overtime and Undertime Management:**
    - "Sets up new rules for calculating overtime hours for employees working on weekends."
    - Set up overtime and undertime calculation rules.
    - Approve or reject overtime requests.
    - Generate reports on overtime and undertime hours.
    - Manage user access and permissions for overtime and undertime data.
- **Official Business and Travel Management:**
    - "Configures a new approval workflow for travel requests requiring CEO approval for international trips."
    - Configure travel policies and approval workflows.
    - Approve or reject travel requests.
    - Generate reports on travel expenses.
    - Manage user access and permissions for travel data.
- **OJT 201 File Management:**
    - "Creates a new OJT record for an employee undergoing training for a new software system."
    - Create and manage OJT records for employees.
    - Track OJT progress and completion.
    - Generate reports on OJT activities.
    - Manage user access and permissions for OJT records.
- **HR Memos and Bulletins:**
    - "Publishes a new memo announcing changes to the company's dress code policy."
    - Create and publish HR memos and bulletins.
    - Manage memo and bulletin distribution lists.
    - Archive past memos and bulletins.
    - Manage user access and permissions for creating and publishing memos and bulletins.
- **Organizational Chart Management:**
    - "Updates the organizational chart to reflect a new department created after a company restructure."
    - Update and maintain the organizational chart.
    - Create and manage positions and reporting relationships.
    - Generate organizational chart reports.
    - Manage user access and permissions for organizational chart data.
- **Crew Movements:**
    - "Approves a crew transfer request for a ship captain moving to a different vessel."
    - Manage and track crew transfers between ships.
    - Approve or reject transfer requests.
    - Generate reports on crew movements.
    - Manage user access and permissions for crew movement data.
- **Job Descriptions:**
    - "Creates a new job description for a newly created role in the IT department."
    - Create and manage job descriptions.
    - Update and revise job descriptions as needed.
    - Manage user access and permissions for job descriptions.
- **Employee Offboarding and Record Retention:**
    - "Initiates the offboarding process for a retiring employee, ensuring compliance with record retention policies."
    - Manage the offboarding process for separated, terminated, or retired employees.
    - Ensure compliance with record retention policies.
    - Manage user access and permissions for offboarding and record retention data.
- **Statutory Compliance:**
    - "Downloads and updates the latest BIR tax tables for accurate withholding calculations."
    - Generate BIR Alpha List reports.
    - Manage SSS maternity leave applications and benefits.
    - Process PhilHealth sick leave benefits claims.
    - Facilitate Pag-IBIG loan applications.
    - Update government agency tables (BIR, SSS, PhilHealth, Pag-IBIG).
    - Manage user access and permissions for statutory compliance data.

### **4.3 HR Staff**

Access to specific HR modules and data based on their responsibilities, such as recruitment, payroll, benefits, or training.

- **Recruitment and Onboarding:**
    - "Posts a new job opening for a Marketing Specialist on the company careers page and LinkedIn."
    - Post job openings and manage job requisitions.
    - Screen applicants and schedule interviews.
    - Onboard new hires and manage onboarding tasks.
    - Generate reports on recruitment activities.
- **Performance Management:**
    - "Conducts a performance review for a team member, providing feedback and setting goals."
    - Conduct performance reviews for their assigned employees.
    - Set performance goals and provide feedback.
    - Generate performance reports for their team members.
- **Compensation and Benefits:**
    - "Processes payroll for the marketing department, ensuring accurate salary and benefits deductions."
    - Process payroll for their assigned employees.
    - Manage benefits enrollment for their team members.
    - Generate payroll and benefits reports for their team.
- **Employee 201 File Management:**
    - "Updates an employee's emergency contact information in their personnel file."
    - Access and update employee records for their assigned team members.
- **Attendance and Leave Management:**
    - "Approves a leave request from a team member for vacation time."
    - Monitor attendance and manage leave requests for their team members.
- **Overtime and Undertime Management:**
    - "Reviews and approves an overtime request from a team member who worked extra hours on a project."
    - Manage overtime and undertime requests for their team members.
- **Official Business and Travel Management:**
    - "Submits a travel request for a team member attending a conference, attaching all necessary documents."
    - Manage travel requests for their team members.
- **OJT 201 File Management:**
    - "Updates an employee's OJT record with their latest training progress and assessment results."
    - Manage OJT records for their team members.
- **HR Memos and Bulletins:**
    - "Reads a newly published HR memo about upcoming changes to the company's health insurance plan."
    - Access and read HR memos and bulletins.
- **Organizational Chart Management:**
    - "Views the organizational chart to understand the reporting structure within their department."
    - View the organizational chart and reporting relationships.
- **Crew Movements:**
    - "Initiates a crew transfer request for a crew member who needs to be reassigned to a different vessel."
    - Initiate crew transfer requests for their team members.
- **Job Descriptions:**
    - "Accesses and reviews the job description for a vacant position before posting a new job opening."
    - Access and review job descriptions for their team members.
- **Employee Offboarding and Record Retention:**
    - "Participates in the offboarding process for a team member who is resigning, conducting an exit interview."
    - Participate in the offboarding process for their team members.
- **Statutory Compliance:**
    - "Accesses and reviews the BIR Alpha List report to ensure accuracy and completeness before submission."
    - Access and review statutory compliance reports.

### **4.4 Manager**

Access to employee data and functionalities relevant to their team members, such as performance reviews, leave approvals, and team reports.

- **Performance Management:**
    - "Reviews and approves performance goals set by a team member for the next quarter."
    - Conduct performance reviews for their team members.
    - Set performance goals and provide feedback.
    - Access performance reports for their team.
- **Attendance and Leave Management:**
    - "Responds to a leave request notification and approves a team member's sick leave."
    - Approve or deny leave requests from their team members.
    - Monitor attendance for their team.
- **Overtime and Undertime Management:**
    - "Reviews and approves an overtime request from a team member who worked late to meet a deadline."
    - Approve or deny overtime requests from their team members.
- **Official Business and Travel Management:**
    - "Receives a notification for a travel request and approves a team member's business trip."
    - Approve or deny travel requests from their team members.
- **Employee 201 File Management:**
    - "Accesses an employee's training records to review their certifications and skills."
    - Access and review employee records for their team members.
- **OJT 201 File Management:**
    - "Accesses and reviews the OJT records for a new team member to assess their training progress."
    - Access and review OJT records for their team members.
- **HR Memos and Bulletins:**
    - "Reads a newly published HR memo about changes to the company's performance bonus policy."
    - Access and read HR memos and bulletins.
- **Organizational Chart Management:**
    - "Views the organizational chart to understand the reporting structure within their team and department."
    - View the organizational chart and reporting relationships for their team.
- **Crew Movements:**
    - "Initiates a crew transfer request for a team member who needs to be reassigned to a different vessel."
    - Initiate crew transfer requests for their team members.
- **Job Descriptions:**
    - "Accesses and reviews the job description for a team member's role to better understand their responsibilities."
    - Access and review job descriptions for their team members.

### **4.5 Employee**

Self-service access to personal information, leave requests, pay stubs, and company policies.

- **Employee and Manager Self-Service:**
    - "Logs in to the HRIS portal to update their personal address and contact details."
    - Update personal information.
    - Submit leave requests.
    - View pay stubs and benefits information.
    - Access company policies and procedures.
- **Employee 201 File Management:**
    - "Accesses and updates their personal information, employment history, and other details in their 201 file, pending verification and approval by HR."
- **Attendance and Leave Management:**
    - "Submits a leave request for upcoming vacation time, selecting the appropriate leave type and dates."
    - View attendance records and leave balances.
- **Performance Management:**
    - "Reviews their performance goals for the current period and tracks progress towards achieving them."
    - View performance reviews and goals.
- **OJT 201 File Management:**
    - "Accesses their OJT records to review their training progress and completed courses."
    - View OJT records.
- **HR Memos and Bulletins:**
    - "Accesses and reads a newly published HR memo about upcoming company events and holidays."
    - Access and read HR memos and bulletins.

## **4.6 Access Permissions**

Access permissions are configured based on user roles to ensure that individuals can only access and modify data relevant to their responsibilities. This prevents unauthorized access and protects sensitive HR information.

This detailed breakdown of user roles and use cases provides a comprehensive understanding of how different users interact with the HRIS and its various modules. This can help in user training, system configuration, and ensuring that everyone utilizes the system effectively within their defined roles.

# **5. Workflows and Processes**

## **5.1 Process Maps**

The HRIS in ABAS v3 may have revised or automated some HR processes. Detailed process maps or flowcharts illustrate the steps involved in key HR processes, such as:

**Recruitment Process:** From creating a job requisition to onboarding a new hire.

figure …

**Performance Review Process:** From setting goals to conducting performance appraisals.

figure …

**Leave Request Process:** From submitting a leave request to approval and recording.

figure …

**Offboarding Process:** From initiating termination to finalizing employee records.

figure …

**Manpower Request Process:** From a department manager submitting a manpower request to HR reviewing, approving, and fulfilling the request.

figure …

## 5.2 Process Automation

ABAS v3 leverages automation to streamline HR workflows, such as:

- **Automated Notifications:** For leave requests, performance reviews, manpower requests, and other HR-related tasks.
- **Automated Approval Workflows:** For leave requests, travel authorizations, manpower requests, and other approvals.
- **Automated Data Entry:** For time and attendance tracking, benefits enrollment, and other data entry tasks.

## **5.3 Processes Initiated Outside HRIS**

While the HRIS manages core HR functions, some processes may be initiated outside the system, such as:

- **Manpower Requests:** Department managers or supervisors may submit manpower requests through a separate system or process, which are then integrated into the HRIS for review and fulfillment.
- **Training Nominations:** Department heads may nominate employees for training programs through a separate process, which is then integrated into the HRIS for tracking and management.
- **Performance Improvement Plans:** Managers may initiate performance improvement plans outside the HRIS, but the plans can be linked to employee records in the system for tracking and monitoring progress.
- **Promotion Requests:** A manager or supervisor may submit a request for an employee's promotion through a separate process, which is then integrated with the HRIS for review, approval, and implementation.
- **Incident Reports:** Employees may submit incident reports through a separate system or process, which are then forwarded to HR for review and appropriate action.
- **Notice to Explain (NTE) Requests:** A manager or supervisor may request HR to issue a Notice to Explain (NTE) to an employee through a separate process. This request is then integrated into the HRIS, allowing HR to document, track, and manage the NTE process, including the employee's response and any subsequent actions.

These processes, while initiated outside the HRIS, are still integrated into the system to ensure a centralized and comprehensive view of HR activities.

## **5.4 Incident Report and NTE Relationship**

The HRIS can establish a relationship between incident reports and NTEs. When an incident report is filed in response to an NTE, the system can tag them as related, allowing HR to track the entire sequence of events and actions taken. This helps to ensure that appropriate disciplinary measures are taken and that all relevant documentation is linked for future reference.

# **6. Use Cases**

This chapter provides detailed descriptions of various use cases for the ABAS v3 HRIS, outlining how different user roles interact with the system to perform specific tasks and achieve desired outcomes. Each use case is presented in a structured format, including:

- **Use Case Name:** A concise name for the use case.
- **Description:** A brief overview of the use case's purpose.
- **Primary Actor:** The main user or role initiating the use case.
- **Goals:** The objectives the primary actor aims to achieve.
- **Stakeholders:** Other users or roles involved in the use case.
- **Pre-conditions:** Conditions that must be met before the use case can begin.
- **Post-conditions:** The expected outcome or state after the use case is completed.
- **Basic Flow:** The typical sequence of steps involved in the use case.
- **Alternate Path:** Any alternative flows or scenarios that may occur during the use case.

These use cases provide a comprehensive understanding of how different user roles interact with the HRIS to perform various HR functions, from applying for leave to managing employee data and ensuring statutory compliance.

## **6.1 Recruitment and Onboarding**

### **6.1.1 Use Case 1: Submit Manpower Request**

- **Use Case Name:** Submit Manpower Request
- **Description:** A department head submits a request for manpower to HR.
- **Primary Actor:** Department Head
- **Goals:** To request additional personnel for the department.
- **Stakeholders:** Department Head, HR Manager, VP/SVP/President
- **Pre-conditions:** Department has a need for additional personnel.
- **Post-conditions:** Manpower request is submitted for approval.
- **Basic Flow:**
    1. Department Head identifies the need for additional personnel. 
    2. Department Head completes a Personnel Requisition Form (PRF). 
    3. Department Head submits the PRF to HR. 
    4. The system sends a notification to the HR Manager. 
- **Alternate Path:**
    1. If the PRF is incomplete or contains errors, the system prompts the Department Head to correct the information. 

### **6.1.2 Use Case 2: Review and Recommend Manpower Request**

- **Use Case Name:** Review and Recommend Manpower Request
- **Description:** HR Manager reviews the manpower request and recommends it for approval.
- **Primary Actor:** HR Manager
- **Goals:** To ensure the validity and justification of the manpower request.
- **Stakeholders:** HR Manager, Department Head, VP/SVP/President
- **Pre-conditions:** A manpower request has been submitted by a Department Head.
- **Post-conditions:** Manpower request is recommended for approval or rejected.
- **Basic Flow:**
    1. HR Manager receives a notification of a manpower request. 
    2. HR Manager reviews the PRF and supporting documents. 
    3. HR Manager recommends the request for approval or rejects it. 
    4. If rejected, HR Manager provides a reason for rejection. 
    5. The system sends a notification to the appropriate approving authority (VP/SVP/President). 
- **Alternate Path:**
    1. If the HR Manager requires additional information, they can request clarification from the Department Head. 

### **6.1.3 Use Case 3: Approve Manpower Request**

- **Use Case Name:** Approve Manpower Request
- **Description:** The appropriate authority approves or rejects the manpower request.
- **Primary Actor:** VP/SVP/President
- **Goals:** To authorize the hiring process for the requested manpower.
- **Stakeholders:** VP/SVP/President, HR Manager, Department Head
- **Pre-conditions:** A manpower request has been reviewed and recommended for approval by the HR Manager.
- **Post-conditions:** Manpower request is approved or rejected, and the HR department is notified.
- **Basic Flow:**
    1. The approving authority receives a notification of a manpower request. 
    2. The approving authority reviews the PRF and recommendations. 
    3. The approving authority approves or rejects the request. 
    4. If rejected, the approving authority provides a reason for rejection. 
    5. The system updates the status of the manpower request and notifies the HR department. 
- **Alternate Path:**
    1. If the approving authority requires additional information, they can request clarification from the HR Manager or Department Head. 

### **6.1.4 Use Case 4: Post Job Vacancy**

- **Use Case Name:** Post Job Vacancy
- **Description:** HR posts the approved job vacancy on relevant platforms.
- **Primary Actor:** HR Staff
- **Goals:** To attract qualified candidates for the vacant position.
- **Stakeholders:** HR Staff, HR Manager, Applicants
- **Pre-conditions:** A manpower request has been approved, and the job description is finalized.
- **Post-conditions:** Job vacancy is posted on internal and external platforms (e.g., company website, job boards, social media).
- **Basic Flow:**
    1. HR Staff receives notification of the approved manpower request. 
    2. HR Staff prepares the job posting with relevant details (job title, description, requirements, etc.). 
    3. HR Staff posts the vacancy on internal and external platforms. 
- **Alternate Path:**
    1. If the job posting needs to be revised or updated, HR Staff can edit the posting accordingly. 

### **6.1.5 Use Case 5: Receive and Screen Applications**

- **Use Case Name:** Receive and Screen Applications
- **Description:** HR receives and screens applications for the vacant position.
- **Primary Actor:** HR Staff
- **Goals:** To identify qualified candidates who meet the job requirements.
- **Stakeholders:** HR Staff, HR Manager, Applicants
- **Pre-conditions:** Job vacancy has been posted, and applications are received.
- **Post-conditions:** Applications are screened, and shortlisted candidates are identified.
- **Basic Flow:**
    1. HR Staff receives applications through various channels (e.g., online, email, walk-in). 
    2. HR Staff reviews applications and screens candidates based on qualifications and experience. 
    3. HR Staff shortlists qualified candidates for further evaluation. 
- **Alternate Path:**
    1. If there are a large number of applications, HR Staff may use automated screening tools to filter candidates based on specific criteria. 

### **6.1.6 Use Case 6: Conduct Interviews**

- **Use Case Name:** Conduct Interviews
- **Description:** HR conducts interviews with shortlisted candidates.
- **Primary Actor:** HR Staff, HR Manager, Department Head
- **Goals:** To assess candidates' skills, experience, and suitability for the position.
- **Stakeholders:** HR Staff, HR Manager, Department Head, Applicants
- **Pre-conditions:** Shortlisted candidates have been identified.
- **Post-conditions:** Candidates are interviewed, and their performance is evaluated.
- **Basic Flow:**
    1. HR Staff schedules interviews with shortlisted candidates. 
    2. HR Staff, HR Manager, and/or Department Head conduct interviews. 
    3. Interviewers evaluate candidates based on pre-defined criteria. 
- **Alternate Path:**
    1. If a candidate is unavailable for an in-person interview, a video conference or phone interview may be conducted. 

### **6.1.7 Use Case 7: Conduct Background Checks**

- **Use Case Name:** Conduct Background Checks
- **Description:** HR conducts background checks on selected candidates.
- **Primary Actor:** HR Staff
- **Goals:** To verify information provided by candidates and ensure their suitability for employment.
- **Stakeholders:** HR Staff, Candidate
- **Pre-conditions:** Candidate has been selected for background check.
- **Post-conditions:** Background check is completed, and results are documented.
- **Basic Flow:**
    1. HR Staff obtains consent from the candidate to conduct a background check. 
    2. HR Staff initiates the background check process, which may include verifying employment history, education, and criminal records. 
    3. HR Staff documents the results of the background check. 
- **Alternate Path:**
    1. If any discrepancies or red flags are found during the background check, HR may investigate further or discuss the findings with the candidate. 

### **6.1.8 Use Case 8: Make Job Offer**

- **Use Case Name:** Make Job Offer
- **Description:** HR makes a job offer to the selected candidate.
- **Primary Actor:** HR Manager
- **Goals:** To formally offer the position to the candidate and obtain their acceptance.
- **Stakeholders:** HR Manager, Candidate
- **Pre-conditions:** Candidate has successfully passed all screening stages, including background checks.
- **Post-conditions:** Job offer is made, and candidate accepts or rejects the offer.
- **Basic Flow:**
    1. HR Manager prepares the job offer letter with details such as salary, benefits, and start date. 
    2. HR Manager sends the job offer letter to the candidate. 
    3. Candidate reviews and accepts or rejects the job offer. 
- **Alternate Path:**
    1. If the candidate requests changes to the job offer, HR Manager negotiates and revises the offer accordingly. 

### **6.1.9 Use Case 9: Onboard New Hire**

- **Use Case Name:** Onboard New Hire
- **Description:** HR onboards the newly hired employee.
- **Primary Actor:** HR Staff
- **Goals:** To integrate the new employee into the company and provide them with necessary information and resources.
- **Stakeholders:** HR Staff, New Hire, Department Head
- **Pre-conditions:** Candidate has accepted the job offer.
- **Post-conditions:** New hire is successfully onboarded and integrated into the company.
- **Basic Flow:**
    1. HR Staff prepares onboarding documents and resources. 
    2. HR Staff conducts orientation and provides necessary information to the new hire. 
    3. HR Staff coordinates with the Department Head for job-specific training and integration. 
- **Alternate Path:**
    1. If the new hire requires additional support or information, HR Staff provides assistance accordingly. 

## **6.2 Performance Management**

### **6.2.1 Use Case 1: Set Performance Goals**

- **Use Case Name:** Set Performance Goals
- **Description:** Managers and employees collaboratively set performance goals for a specific period.
- **Primary Actor:** Manager, Employee
- **Goals:** To establish clear expectations and objectives for employee performance, aligned with company goals.
- **Stakeholders:** Manager, Employee, HR
- **Pre-conditions:** Performance standards and evaluation criteria are defined.
- **Post-conditions:** Performance goals are documented and agreed upon.
- **Basic Flow:**
    1. Manager initiates the goal-setting process, providing context and expectations.
    2. Employee proposes goals based on their role and responsibilities.
    3. Manager and employee discuss and finalize goals, ensuring they are SMART (Specific, Measurable, Achievable, Relevant, Time-bound).
    4. Goals are documented in the HRIS, linked to the employee's performance record.
- **Alternate Path:**
    1. If there is disagreement on goals, the manager and employee may consult with HR for guidance.

### **6.2.2 Use Case 2: Conduct Performance Review**

- **Use Case Name:** Conduct Performance Review
- **Description:** Managers conduct performance reviews to evaluate employee performance against set goals.
- **Primary Actor:** Manager
- **Goals:** To assess employee performance, provide feedback, and identify areas for improvement.
- **Stakeholders:** Manager, Employee, HR
- **Pre-conditions:** Performance goals have been set, and the review period has ended.
- **Post-conditions:** Performance review is completed, and feedback is provided to the employee.
- **Basic Flow:**
    1. Manager gathers data and evidence on employee performance.
    2. Manager schedules a meeting with the employee for the performance review.
    3. Manager discusses performance with the employee, providing feedback on strengths and areas for improvement.
    4. Employee provides self-evaluation and feedback.
    5. Manager and employee agree on performance ratings and development plans.
    6. Performance review is documented and stored in the HRIS.
- **Alternate Path:**
    1. If there are significant performance issues, the manager may initiate a performance improvement plan.

### **6.2.3 Use Case 3: Provide Performance Feedback**

- **Use Case Name:** Provide Performance Feedback
- **Description:** Managers provide ongoing feedback to employees on their performance.
- **Primary Actor:** Manager
- **Goals:** To reinforce positive behaviors, address performance gaps promptly, and support employee development.
- **Stakeholders:** Manager, Employee
- **Pre-conditions:** Manager observes employee performance or receives feedback from others.
- **Post-conditions:** Feedback is provided to the employee, and any necessary actions are discussed.
- **Basic Flow:**
    1. Manager observes employee performance or receives feedback from others.
    2. Manager provides specific and timely feedback to the employee, focusing on behaviors and outcomes.
    3. Manager and employee discuss any necessary adjustments or development plans.
- **Alternate Path:**
    1. If the feedback is negative, the manager may need to document the conversation and follow up with additional support or coaching.

## **6.3 Compensation and Benefits**

### **6.3.1 Use Case 1: Process Payroll**

- **Use Case Name:** Process Payroll
- **Description:** HR processes employee payroll, including calculating salaries, deductions, and taxes.
- **Primary Actor:** HR Staff, Payroll Master, Payroll Specialist
- **Goals:** To ensure accurate and timely payment of salaries and compliance with tax and statutory regulations.
- **Stakeholders:** HR Staff, Payroll Master, Payroll Specialist, Employees, Finance Department, Government Agencies (BIR, SSS, PhilHealth, Pag-IBIG)
- **Pre-conditions:** Employee timekeeping and attendance data is collected and verified.
- **Post-conditions:** Payroll is processed, and salaries are paid to employees.
- **Basic Flow:**
    1. HR Staff collects and verifies employee timekeeping and attendance data.
    2. Payroll Master prepares the payroll register, calculating gross pay, deductions, and net pay for each employee.
    3. Payroll Specialist reviews and verifies the payroll register, ensuring accuracy and compliance with tax and statutory regulations.
    4. HR Manager approves the payroll register.
    5. Finance Department releases the payroll funds.
    6. HR disburses salaries to employees through designated channels (e.g., bank transfer, cash).
    7. HR generates payroll reports and submits statutory contributions to government agencies.
- **Alternate Path:**
    1. If there are errors or discrepancies in the payroll data, the Payroll Specialist or HR Staff corrects the data and reprocesses the payroll.

### **6.3.2 Use Case 2: Manage Benefits Enrollment**

- **Use Case Name:** Manage Benefits Enrollment
- **Description:** HR manages employee benefits enrollment, including open enrollment periods, new hire enrollment, and qualifying life events.
- **Primary Actor:** HR Staff, HR Manager
- **Goals:** To ensure employees are properly enrolled in benefit plans and that their benefits information is up-to-date.
- **Stakeholders:** HR Staff, HR Manager, Employees, Benefits Providers
- **Pre-conditions:** Benefits plans and eligibility criteria are defined.
- **Post-conditions:** Employees are enrolled in benefits plans, and their information is updated in the HRIS.
- **Basic Flow:**
    1. HR communicates benefits information and open enrollment periods to employees.
    2. Employees enroll in or make changes to their benefit elections through the HRIS.
    3. HR reviews and approves benefit enrollments.
    4. HR transmits enrollment data to benefits providers.
    5. HR updates employee benefits information in the HRIS.
- **Alternate Path:**
    1. If an employee experiences a qualifying life event (e.g., marriage, birth of a child), they can initiate a change in benefits enrollment outside of the open enrollment period.

### **6.3.3 Use Case 3: Process Benefits Claims**

- **Use Case Name:** Process Benefits Claims
- **Description:** HR processes employee benefit claims, such as medical, dental, and vision claims.
- **Primary Actor:** HR Staff
- **Goals:** To ensure that employee benefit claims are processed accurately and efficiently.
- **Stakeholders:** HR Staff, Employees, Benefits Providers
- **Pre-conditions:** Employee has submitted a benefit claim.
- **Post-conditions:** Benefit claim is processed, and payment or denial is communicated to the employee.
- **Basic Flow:**
    1. HR receives the benefit claim from the employee.
    2. HR verifies the claim and supporting documentation.
    3. HR submits the claim to the benefits provider.
    4. Benefits provider processes the claim and notifies HR of the decision.
    5. HR communicates the claim decision and any payment details to the employee.
- **Alternate Path:**
    1. If the claim is denied, HR explains the reason for denial and assists the employee with any appeals or further action.

## **6.4 Employee 201 File Management**

### **6.4.1 Use Case 1: Create Employee Record**

- **Use Case Name:** Create Employee Record
- **Description:** HR creates a new employee record in the HRIS.
- **Primary Actor:** HR Staff
- **Goals:** To capture and store essential employee information for HR processes and record-keeping.
- **Stakeholders:** HR Staff, Employee
- **Pre-conditions:** New employee has been hired.
- **Post-conditions:** Employee record is created in the HRIS.
- **Basic Flow:**
    1. HR gathers employee information (e.g., personal details, contact information, employment history, emergency contacts).
    2. HR enters the information into the HRIS, creating a new employee record.
    3. HR attaches relevant documents (e.g., resume, contracts) to the employee record.
- **Alternate Path:**
    1. If any information is missing or incomplete, HR follows up with the employee to obtain the necessary details.

### **6.4.2 Use Case 2: Update Employee Record**

- **Use Case Name:** Update Employee Record
- **Description:** HR or an employee updates information in an existing employee record.
- **Primary Actor:** HR Staff, Employee
- **Goals:** To maintain accurate and up-to-date employee information.
- **Stakeholders:** HR Staff, Employee
- **Pre-conditions:** Employee record exists in the HRIS.
- **Post-conditions:** Employee record is updated with the new information.
- **Basic Flow:**
    1. HR or employee identifies the need to update information in the employee record (e.g., change of address, promotion, new skills).
    2. HR or employee accesses the employee record in the HRIS.
    3. HR or employee updates the relevant information and saves the changes.
    4. If the employee updates the information, HR reviews and approves the changes.
- **Alternate Path:**
    1. If there are any discrepancies or inconsistencies in the updated information, HR clarifies the details with the employee.

### **6.4.3 Use Case 3: Access Employee Record**

- **Use Case Name:** Access Employee Record
- **Description:** Authorized users access employee records to view or retrieve information.
- **Primary Actor:** HR Staff, HR Manager, Department Head, Employee (limited access)
- **Goals:** To obtain employee information for HR processes, decision-making, or personal reference.
- **Stakeholders:** HR Staff, HR Manager, Department Head, Employee
- **Pre-conditions:** User has appropriate access permissions.
- **Post-conditions:** User views or retrieves the requested employee information.
- **Basic Flow:**
    1. User logs into the HRIS and navigates to the "Employee 201 File Management" module.
    2. User searches for and selects the desired employee record.
    3. User views or retrieves the necessary information from the record.
- **Alternate Path:**
    1. If the user does not have sufficient access permissions, the system restricts access to certain information or the entire record.

## **6.5 Attendance and Leave Management**

*(Leave Management Use Cases from previous responses)*

## **6.6 Overtime and Undertime Management**

**6.6.1 Use Case 1: Request Overtime**

- **Use Case Name:** Request Overtime
- **Description:** An employee requests authorization for overtime work.
- **Primary Actor:** Employee
- **Goals:** To obtain approval for working overtime and ensure proper compensation.
- **Stakeholders:** Employee, Department Head, HR
- **Pre-conditions:** Employee has a valid reason for working overtime (e.g., project deadline, urgent task).
- **Post-conditions:** Overtime request is submitted, and status is pending approval.
- **Basic Flow:**
    1. Employee logs into the HRIS portal.
    2. Employee navigates to the "Overtime Request" section.
    3. Employee enters the date, start and end times, and reason for overtime.
    4. Employee submits the overtime request.
    5. The system sends a notification to the Department Head.
- **Alternate Path:**
    1. If the overtime request exceeds a certain threshold or violates company policies, the system may require additional approval from HR or higher management.

**6.6.2 Use Case 2: Approve Overtime**

- **Use Case Name:** Approve Overtime
- **Description:** A Department Head reviews and approves/denies an employee's overtime request.
- **Primary Actor:** Department Head
- **Goals:** To authorize or deny overtime requests based on business needs and company policies.
- **Stakeholders:** Department Head, Employee, HR
- **Pre-conditions:** An overtime request has been submitted by an employee.
- **Post-conditions:** Overtime request is approved or denied, and the employee is notified.
- **Basic Flow:**
    1. Department Head receives a notification of an overtime request.
    2. Department Head reviews the request details (date, time, reason).
    3. Department Head approves or denies the request.
    4. If denied, the Department Head provides a reason for denial.
    5. The system updates the overtime request status and notifies the employee.
- **Alternate Path:**
    1. If the Department Head needs more information, they can request clarification from the employee before making a decision.

**6.6.3 Use Case 3: Record Overtime**

- **Use Case Name:** Record Overtime
- **Description:** HR records approved overtime hours in the system for payroll processing.
- **Primary Actor:** HR Appointed Personnel
- **Goals:** To ensure accurate record-keeping of overtime hours for payroll calculations.
- **Stakeholders:** HR Appointed Personnel, Employee, Department Head
- **Pre-conditions:** An overtime request has been approved by the Department Head.
- **Post-conditions:** Overtime hours are recorded in the system.
- **Basic Flow:**
    1. HR receives notification of approved overtime request.
    2. HR verifies the overtime details and enters the hours into the system.
- **Alternate Path:**
    1. If there is a discrepancy in the overtime details, HR contacts the Department Head for clarification.

## **6.7 Official Business and Travel Management**

### **6.7.1 Use Case 1: Request Travel**

- **Use Case Name:** Request Travel
- **Description:** An employee requests authorization for business travel.
- **Primary Actor:** Employee
- **Goals:** To obtain approval for business travel and arrange necessary logistics.
- **Stakeholders:** Employee, Department Head, HR, Finance Department
- **Pre-conditions:** Employee has a valid reason for business travel (e.g., conference, client meeting).
- **Post-conditions:** Travel request is submitted, and status is pending approval.
- **Basic Flow:**
    1. Employee logs into the HRIS portal.
    2. Employee navigates to the "Travel Request" section.
    3. Employee enters the destination, purpose, dates, and estimated expenses for the trip.
    4. Employee submits the travel request.
    5. The system sends a notification to the Department Head.
- **Alternate Path:**
    1. If the travel request exceeds a certain budget or requires additional approvals, the system routes the request accordingly.

### **6.7.2 Use Case 2: Approve Travel**

- **Use Case Name:** Approve Travel
- **Description:** A Department Head or other authorized personnel reviews and approves/denies an employee's travel request.
- **Primary Actor:** Department Head, HR Manager, Finance Department
- **Goals:** To authorize or deny travel requests based on business needs, budget, and company policies.
- **Stakeholders:** Department Head, HR Manager, Finance Department, Employee
- **Pre-conditions:** A travel request has been submitted by an employee.
- **Post-conditions:** Travel request is approved or denied, and the employee is notified.
- **Basic Flow:**
    1. The approver receives a notification of a travel request.
    2. The approver reviews the request details (destination, purpose, dates, expenses).
    3. The approver approves or denies the request.
    4. If denied, the approver provides a reason for denial.
    5. The system updates the travel request status and notifies the employee.
- **Alternate Path:**
    1. If the approver needs more information, they can request clarification from the employee before making a decision.

### **6.7.3 Use Case 3: Arrange Travel Logistics**

- **Use Case Name:** Arrange Travel Logistics
- **Description:** HR or a designated travel coordinator arranges travel logistics for approved trips.
- **Primary Actor:** HR Staff, Travel Coordinator
- **Goals:** To book flights, accommodations, and other travel arrangements for employees on business trips.
- **Stakeholders:** HR Staff, Travel Coordinator, Employee, Travel Agencies
- **Pre-conditions:** A travel request has been approved.
- **Post-conditions:** Travel arrangements are booked and confirmed.
- **Basic Flow:**
    1. HR or Travel Coordinator receives notification of approved travel request.
    2. HR or Travel Coordinator coordinates with the employee to determine travel preferences and requirements.
    3. HR or Travel Coordinator books flights, accommodations, and other travel services through a travel agency or online platform.
    4. HR or Travel Coordinator provides the employee with travel documents and information.
- **Alternate Path:**
    1. If there are changes to the travel itinerary or unexpected issues arise, HR or Travel Coordinator adjusts the arrangements accordingly.

### **6.7.4 Use Case 4: Process Travel Expenses**

- **Use Case Name:** Process Travel Expenses
- **Description:** HR processes employee travel expense reports for reimbursement.
- **Primary Actor:** HR Staff, Finance Department
- **Goals:** To reimburse employees for eligible travel expenses incurred during business trips.
- **Stakeholders:** HR Staff, Finance Department, Employee
- **Pre-conditions:** Employee has submitted a travel expense report.
- **Post-conditions:** Travel expenses are reviewed, approved, and reimbursed.
- **Basic Flow:**
    1. Employee submits a travel expense report with supporting documentation (e.g., receipts).
    2. HR reviews and verifies the expense report for accuracy and compliance with company policies.
    3. HR approves the expense report and forwards it to the Finance Department for processing.
    4. Finance Department reimburses the employee for eligible expenses.
- **Alternate Path:**
    1. If there are any discrepancies or ineligible expenses, HR clarifies the details with the employee and adjusts the expense report accordingly.

## **6.8 OJT 201 File Management**

### **6.8.1 Use Case 1: Create OJT Record**

- **Use Case Name:** Create OJT Record
- **Description:** HR creates a new On-the-Job Training (OJT) record for an employee.
- **Primary Actor:** HR Staff, Department Head
- **Goals:** To document and track employee OJT activities and progress.
- **Stakeholders:** HR Staff, Department Head, Employee
- **Pre-conditions:** Employee has been assigned to an OJT program.
- **Post-conditions:** OJT record is created in the HRIS.
- **Basic Flow:**
    1. HR or Department Head initiates the creation of an OJT record for the employee.
    2. HR or Department Head enters the OJT details, including the program name, start and end dates, objectives, and assigned mentor or supervisor.
    3. The system creates the OJT record and links it to the employee's profile.
- **Alternate Path:**
    1. If the OJT program requires specific pre-requisites or approvals, the system ensures that these are met before creating the record.

### **6.8.2 Use Case 2: Update OJT Record**

- **Use Case Name:** Update OJT Record
- **Description:** HR or the assigned mentor/supervisor updates the employee's OJT record with progress and evaluations.
- **Primary Actor:** HR Staff, Department Head, Mentor/Supervisor
- **Goals:** To track the employee's OJT progress, document evaluations, and provide feedback.
- **Stakeholders:** HR Staff, Department Head, Mentor/Supervisor, Employee
- **Pre-conditions:** OJT record exists in the HRIS.
- **Post-conditions:** OJT record is updated with progress and evaluation details.
- **Basic Flow:**
    1. HR, Department Head, or Mentor/Supervisor accesses the employee's OJT record in the HRIS.
    2. They enter updates on the employee's progress, including completed tasks, achievements, and challenges.
    3. They document evaluations of the employee's performance during the OJT program.
    4. They provide feedback to the employee through the system or in-person meetings.
- **Alternate Path:**
    1. If the employee's performance during OJT is not satisfactory, the mentor/supervisor may recommend additional training or support.

### **6.8.3 Use Case 3: Access OJT Records**

- **Use Case Name:** Access OJT Records
- **Description:** Authorized users access employee OJT records to review training progress and evaluations.
- **Primary Actor:** HR Staff, HR Manager, Department Head, Employee (limited access)
- **Goals:** To monitor employee OJT progress, assess training effectiveness, and make informed decisions about employee development.
- **Stakeholders:** HR Staff, HR Manager, Department Head, Employee
- **Pre-conditions:** User has appropriate access permissions.
- **Post-conditions:** User views or retrieves the requested OJT information.
- **Basic Flow:**
    1. User logs into the HRIS and navigates to the "OJT 201 File Management" module.
    2. User searches for and selects the desired employee's OJT record.
    3. User views or retrieves the necessary information from the record, including training progress, evaluations, and feedback.
- **Alternate Path:**
    1. If the user does not have sufficient access permissions, the system restricts access to certain information or the entire record.

## **6.9 HR Memos and Bulletins**

### **6.9.1 Use Case 1: Publish HR Memo**

- **Use Case Name:** Publish HR Memo
- **Description:** HR publishes a memo to communicate important information or announcements to employees.
- **Primary Actor:** HR Staff
- **Goals:** To effectively disseminate information to employees.
- **Stakeholders:** HR Staff, Employees
- **Pre-conditions:** HR has information or announcements to share with employees.
- **Post-conditions:** Memo is published and accessible to employees.
- **Basic Flow:**
    1. HR Staff prepares the memo content.
    2. HR Staff logs into the HRIS and navigates to the "HR Memos and Bulletins" module.
    3. HR Staff creates a new memo entry and enters the memo details, including title, content, and target audience.
    4. HR Staff publishes the memo, making it accessible to employees through the HRIS portal or other designated channels.
- **Alternate Path:**
    1. If the memo needs to be revised or updated, HR Staff can edit the memo accordingly.

### **6.9.2 Use Case 2: Access HR Memos**

- **Use Case Name:** Access HR Memos
- **Description:** Employees access and read HR memos and bulletins.
- **Primary Actor:** Employee
- **Goals:** To stay informed about company policies, announcements, and other relevant information.
- **Stakeholders:** Employees, HR Staff
- **Pre-conditions:** HR has published memos or bulletins.
- **Post-conditions:** Employee views and reads the available memos and bulletins.
- **Basic Flow:**
    1. Employee logs into the HRIS portal.
    2. Employee navigates to the "HR Memos and Bulletins" section.
    3. Employee views and reads the available memos and bulletins.
- **Alternate Path:**
    1. If the employee wants to search for specific memos or filter them by category or date, they can use the search and filter functions in the module.

## **6.10 Organizational Chart Management**

### **6.10.1 Use Case 1: View Organizational Chart**

- **Use Case Name:** View Organizational Chart
- **Description:** Employees view the company's organizational chart to understand the company's structure and reporting relationships.
- **Primary Actor:** Employee
- **Goals:** To gain a clear understanding of the company's hierarchy and reporting lines.
- **Stakeholders:** Employees
- **Pre-conditions:** The organizational chart is updated and maintained in the HRIS.
- **Post-conditions:** Employee views the organizational chart.
- **Basic Flow:**
    1. Employee logs into the HRIS portal.
    2. Employee navigates to the "Organizational Chart" section.
    3. Employee views the organizational chart, which may be interactive and allow for zooming and exploring different departments and levels.
- **Alternate Path:**
    1. If the employee wants to search for a specific employee or department, they can use the search function within the organizational chart module.

### **6.10.2 Use Case 2: Update Organizational Chart**

- **Use Case Name:** Update Organizational Chart
- **Description:** HR updates the organizational chart to reflect changes in company structure or reporting relationships.
- **Primary Actor:** HR Staff
- **Goals:** To maintain an accurate and up-to-date organizational chart.
- **Stakeholders:** HR Staff, Employees
- **Pre-conditions:** Changes in company structure or reporting relationships have occurred.
- **Post-conditions:** Organizational chart is updated in the HRIS.
- **Basic Flow:**
    1. HR identifies the need to update the organizational chart (e.g., new hire, promotion, department restructure).
    2. HR accesses the "Organizational Chart Management" module in the HRIS.
    3. HR makes the necessary changes to the chart, such as adding new positions, updating reporting lines, or removing employees who have left the company.
    4. HR saves the updated organizational chart.
- **Alternate Path:**
    1. If there are complex changes to the organizational structure, HR may need to consult with department heads or senior management to ensure accuracy.

## **6.11 Crew Movements**

### **6.11.1 Use Case 1: Request Crew Transfer**

- **Use Case Name:** Request Crew Transfer
- **Description:** A manager or crew member requests a transfer to a different vessel or department.
- **Primary Actor:** Manager, Crew Member
- **Goals:** To initiate a crew transfer for operational or personal reasons.
- **Stakeholders:** Manager, Crew Member, HR, Vessel Master
- **Pre-conditions:** There is a need for a crew transfer (e.g., operational requirements, employee request).
- **Post-conditions:** Crew transfer request is submitted, and status is pending approval.
- **Basic Flow:**
    1. Manager or Crew Member initiates a crew transfer request through the HRIS.
    2. They specify the reason for the transfer, the desired vessel or department, and any other relevant details.
    3. The system sends a notification to the relevant approvers (e.g., HR, Vessel Master).
- **Alternate Path:**
    1. If the transfer request conflicts with operational requirements or company policies, the system may display an error message or require additional approvals.

### **6.11.2 Use Case 2: Approve Crew Transfer**

- **Use Case Name:** Approve Crew Transfer
- **Description:** HR or Vessel Master reviews and approves/denies a crew transfer request.
- **Primary Actor:** HR Staff, Vessel Master
- **Goals:** To authorize or deny crew transfer requests based on operational needs, crew member qualifications, and company policies.
- **Stakeholders:** HR Staff, Vessel Master, Manager, Crew Member
- **Pre-conditions:** A crew transfer request has been submitted.
- **Post-conditions:** Crew transfer request is approved or denied, and the requester is notified.
- **Basic Flow:**
    1. HR or Vessel Master receives a notification of a crew transfer request.
    2. They review the request details and assess the feasibility and impact of the transfer.
    3. They approve or deny the request.
    4. If denied, they provide a reason for denial.
    5. The system updates the request status and notifies the requester.
- **Alternate Path:**
    1. If there are any concerns or conflicts regarding the transfer, HR or Vessel Master may discuss the matter with the relevant parties before making a decision.

### **6.11.3 Use Case 3: Process Crew Transfer**

- **Use Case Name:** Process Crew Transfer
- **Description:** HR processes the approved crew transfer, updating employee records and coordinating logistics.
- **Primary Actor:** HR Staff
- **Goals:** To implement the crew transfer and ensure a smooth transition for the crew member.
- **Stakeholders:** HR Staff, Crew Member, Department Heads, Vessel Master
- **Pre-conditions:** A crew transfer request has been approved.
- **Post-conditions:** Crew member is transferred to the new vessel or department.
- **Basic Flow:**
    1. HR receives notification of the approved crew transfer request.
    2. HR updates the crew member's record in the HRIS, reflecting the new assignment and effective date.
    3. HR coordinates with relevant departments (e.g., payroll, training) to ensure a smooth transition for the crew member.
    4. HR communicates the transfer details to the crew member and relevant stakeholders.
- **Alternate Path:**
    1. If there are any logistical challenges or unexpected issues, HR addresses them promptly to facilitate the transfer.

## **6.12 Job Descriptions**

*(Placeholder for Job Descriptions Use Cases)*

## **6.13 Employee Offboarding and Record Retention**

### **6.13.1 Use Case 1: Resign from Company**

- **Use Case Name:** Resign from Company
- **Description:** An employee voluntarily resigns from the company.
- **Primary Actor:** Employee
- **Goals:** To formally notify the company of their resignation and complete the necessary procedures.
- **Stakeholders:** Employee, Department Head, HR Staff, HR Manager, Finance Department
- **Pre-conditions:** Employee has decided to resign.
- **Post-conditions:** Resignation is acknowledged, clearance is processed, and final pay is settled.
- **Basic Flow:**
    1. Employee prepares a resignation letter stating the reason and effective date.
    2. Employee submits the resignation letter to their Department Head.
    3. Department Head acknowledges the resignation and conducts an exit interview.
    4. Department Head forwards the resignation letter to HR.
    5. HR acknowledges the resignation and conducts an exit interview.
    6. HR generates an exit clearance checklist for the employee.
    7. Employee completes the exit clearance process, settling all accountabilities.
    8. Department Head verifies and signs the exit clearance checklist.
    9. HR prepares the final pay computation and any applicable benefits.
    10. Finance Department releases the final pay to the employee.
    11. HR issues the employment certificate and other relevant documents.
    12. HR updates employee records in the HRIS and archives the employee's file.
- **Alternate Path:**
    1. If the employee withdraws their resignation, the process is terminated, and their employment continues.

### **6.13.2 Use Case 2: Terminate Employment**

- **Use Case Name:** Terminate Employment
- **Description:** The company terminates an employee's employment for a valid reason.
- **Primary Actor:** HR Manager
- **Goals:** To legally and properly terminate an employee's employment.
- **Stakeholders:** HR Manager, Employee, Department Head, Legal Counsel (if applicable), Finance Department
- **Pre-conditions:** There is a valid and documented reason for termination (e.g., misconduct, poor performance, redundancy).
- **Post-conditions:** Employee is notified of termination, clearance is processed, and final pay is settled.
- **Basic Flow:**
    1. HR Manager, in consultation with the Department Head and Legal Counsel (if applicable), prepares a Notice of Termination stating the reason and effective date.
    2. HR Manager issues the Notice of Termination to the employee.
    3. HR Manager conducts an exit interview with the employee.
    4. HR generates an exit clearance checklist for the employee.
    5. Employee completes the exit clearance process, settling all accountabilities.
    6. Department Head verifies and signs the exit clearance checklist.
    7. HR prepares the final pay computation and any applicable benefits.
    8. Finance Department releases the final pay to the employee.
    9. HR issues the employment certificate and other relevant documents.
    10. HR updates employee records in the HRIS and archives the employee's file.
- **Alternate Path:**
    1. If the employee contests the termination, the case may be escalated to a higher authority or legal proceedings.

### **6.13.3 Use Case 3: Process Retirement**

- **Use Case Name:** Process Retirement
- **Description:** HR processes the retirement of an employee.
- **Primary Actor:** HR Appointed Personnel
- **Goals:** To facilitate the employee's retirement and ensure they receive their retirement benefits.
- **Stakeholders:** HR Appointed Personnel, Employee, SSS/GSIS
- **Pre-conditions:** Employee has reached the eligible retirement age or meets other retirement criteria.
- **Post-conditions:** Retirement is processed, and retirement benefits are paid out.
- **Basic Flow:**
    1. Employee informs HR of their intention to retire.
    2. HR verifies the employee's eligibility for retirement.
    3. HR prepares the necessary retirement documents.
    4. Employee completes the exit clearance process.
    5. HR coordinates with SSS/GSIS for the processing of retirement benefits.
    6. HR facilitates the payment of retirement benefits to the employee.
    7. HR updates employee records in the HRIS and archives the employee's file.
- **Alternate Path:**
    1. If the employee is not eligible for retirement, HR informs the employee and discusses alternative options.

## **6.14 Statutory Compliance**

### **6.14.1 Use Case 1: Generate BIR Alpha List**

- **Use Case Name:** Generate BIR Alpha List
- **Description:** HR generates the BIR Alpha List report for submission to the Bureau of Internal Revenue (BIR).
- **Primary Actor:** HR Appointed Personnel
- **Goals:** To comply with BIR requirements for annual reporting of employee income and taxes withheld.
- **Stakeholders:** HR Appointed Personnel, BIR
- **Pre-conditions:** Payroll data for the year is complete and accurate.
- **Post-conditions:** BIR Alpha List report is generated and submitted to BIR.
- **Basic Flow:**
    1. HR accesses the "Statutory Reports" module in the HRIS.
    2. HR selects the "BIR Alpha List" report and specifies the reporting year.
    3. The system generates the BIR Alpha List report, including employee information, income, and taxes withheld.
    4. HR reviews the report for accuracy and completeness.
    5. HR submits the report to BIR through the appropriate channels (e.g., online filing, manual submission).
- **Alternate Path:**
    1. If there are errors or discrepancies in the report, HR corrects the data and regenerates the report before submission.

### **6.14.2 Use Case 2: Process SSS Maternity Benefits**

- **Use Case Name:** Process SSS Maternity Benefits
- **Description:** HR processes maternity benefit claims for eligible employees.
- **Primary Actor:** HR Appointed Personnel
- **Goals:** To facilitate the maternity benefit application and ensure timely payment to eligible employees.
- **Stakeholders:** HR Appointed Personnel, Pregnant Employee, SSS
- **Pre-conditions:** Employee has filed a maternity benefit application and meets the eligibility requirements.
- **Post-conditions:** Maternity benefits are processed and paid out to the employee.
- **Basic Flow:**
    1. HR receives the maternity benefit application from the employee.
    2. HR verifies the employee's eligibility based on SSS requirements.
    3. HR prepares and submits the required documents to SSS.
    4. SSS processes the application and releases the maternity benefits.
    5. HR receives the maternity benefits from SSS and disburses them to the employee.
- **Alternate Path:**
    1. If the application is rejected by SSS, HR informs the employee and explains the reason for rejection.

### **6.14.3 Use Case 3: Process PhilHealth Sickness Benefits**

- **Use Case Name:** Process PhilHealth Sickness Benefits
- **Description:** HR processes sickness benefit claims for eligible employees.
- **Primary Actor:** HR Appointed Personnel
- **Goals:** To facilitate the sickness benefit application and ensure timely payment to eligible employees.
- **Stakeholders:** HR Appointed Personnel, Employee, PhilHealth
- **Pre-conditions:** Employee has filed a sickness benefit application and meets the eligibility requirements.
- **Post-conditions:** Sickness benefits are processed and paid out to the employee.
- **Basic Flow:**
    1. HR receives the sickness benefit application from the employee.
    2. HR verifies the employee's eligibility based on PhilHealth requirements.
    3. HR prepares and submits the required documents to PhilHealth.
    4. PhilHealth processes the application and releases the sickness benefits.
    5. HR receives the sickness benefits from PhilHealth and disburses them to the employee.
- **Alternate Path:**
    1. If the application is rejected by PhilHealth, HR informs the employee and explains the reason for rejection.

### **6.14.4 Use Case 4: Process Pag-IBIG Calamity Loan**

- **Use Case Name:** Process Pag-IBIG Calamity Loan
- **Description:** HR processes calamity loan applications for eligible employees.
- **Primary Actor:** HR Appointed Personnel
- **Goals:** To facilitate the calamity loan application and ensure timely disbursement to eligible employees.
- **Stakeholders:** HR Appointed Personnel, Employee, Pag-IBIG
- **Pre-conditions:** Employee has filed a calamity loan application and meets the eligibility requirements.
- **Post-conditions:** Calamity loan is processed and disbursed to the employee.
- **Basic Flow:**
    1. HR receives the calamity loan application from the employee.
    2. HR verifies the employee's eligibility based on Pag-IBIG requirements and the declared calamity.
    3. HR prepares and submits the required documents to Pag-IBIG.
    4. Pag-IBIG processes the application and releases the calamity loan.
    5. HR receives the calamity loan from Pag-IBIG and disburses it to the employee.
- **Alternate Path:**
    1. If the application is rejected by Pag-IBIG, HR informs the employee and explains the reason for rejection.

### **6.14.5 Use Case 5: Update Government Agency Tables**

- **Use Case Name:** Update Government Agency Tables
- **Description:** HR updates the tables for BIR, SSS, PhilHealth, and Pag-IBIG in the HRIS to reflect the latest regulations and contribution rates.
- **Primary Actor:** HR Appointed Personnel
- **Goals:** To ensure that the HRIS uses the most up-to-date information for statutory compliance calculations.
- **Stakeholders:** HR Appointed Personnel, BIR, SSS, PhilHealth, Pag-IBIG
- **Pre-conditions:** New regulations or contribution rates have been released by the government agencies.
- **Post-conditions:** HRIS tables are updated with the latest information.
- **Basic Flow:**
    1. HR receives notifications or updates from BIR, SSS, PhilHealth, and Pag-IBIG regarding new regulations or contribution rates.
    2. HR accesses the "System Settings" module in the HRIS.
    3. HR updates the relevant tables with the new information.
- **Alternate Path:**
    1. If there are any issues with updating the tables, HR consults with the IT department or the respective government agencies for assistance.

# **7. Conclusion**

The ABAS v3 HRIS represents a significant advancement in the organization's HR capabilities. By streamlining processes, improving data accuracy, and empowering employees and managers, the HRIS contributes to a more efficient, effective, and strategic HR function. The system's comprehensive modules, robust reporting and analytics, and strong data management practices enable HR professionals to make informed decisions, improve compliance, and enhance the overall employee experience.

As the organization continues to evolve, the ABAS v3 HRIS will play a vital role in supporting its growth and success. Future development may include additional modules, enhanced functionalities, and further integration with other systems to meet the organization's evolving HR needs.