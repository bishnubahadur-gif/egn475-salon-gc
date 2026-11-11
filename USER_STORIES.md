# Nexa Salon — User Stories and Acceptance Criteria

EGN 475 — Week 2 Assignment 2.1
Student: Bishnu Bahadur GC
Project: Nexa Salon (Option B — Salon Booking)

## US-01 — View Services
Priority: Must

As a salon client, I want to view available services with prices and durations so that I can choose a service that fits my needs.

- Given active services exist, when I open the services page, then I see their names, prices, and estimated durations.
- Given no services are available, when I open the services page, then I see a clear message that no services are available.

## US-02 — View Available Times
Priority: Must

As a salon client, I want to see available appointment times for a selected service and date so that I can choose a suitable time.

- Given open appointment times exist, when I select a service and date, then I see only available times.
- Given 10:00 AM is already booked, when I view available times for that date, then 10:00 AM is not offered.

## US-03 — Select Stylist
Priority: Should

As a salon client, I want to choose an available stylist so that I can book with someone I prefer.

- Given I have selected a service and appointment time, when I view the stylist options, then I see only stylists who provide that service and are available at that time.
- Given no stylist is available for my selected service and time, when I view the stylist options, then I see a message asking me to choose another time.

## US-04 — Submit Booking Request
Priority: Must

As a salon client, I want to submit an appointment request so that staff can confirm my booking.

- Given I have entered valid contact details and selected an available service and time, when I submit my request, then I receive a booking-request confirmation.
- Given my contact details are missing, when I submit my request, then I see a validation message and the request is not submitted.

## US-05 — View My Appointments
Priority: Must

As a salon client, I want to view my appointments so that I can keep track of upcoming bookings.

-- Given I have an existing appointment and its booking reference, when I enter the reference and matching email address, then I can view the appointment's service, date, time, and status.
- Given I enter an incorrect booking reference or an email address that does not match the appointment, when I request my appointment details, then the system displays an error without revealing another client's information.

## US-06 — Request Cancellation
Priority: Should

As a salon client, I want to request cancellation of an upcoming appointment so that I can notify the salon when I cannot attend.

- Given I have an upcoming confirmed appointment and provide its booking reference and matching email, when I request cancellation, then the appointment is marked Cancellation Requested and staff can review it.
- Given an appointment is already completed or canceled, when I attempt to request cancellation, then the system rejects the request and displays an explanation.

## US-07 — Request Rescheduling
Priority: Should

As a salon client, I want to request a different available time for an appointment so that I can adjust my schedule.

- Given I have an upcoming appointment and provide its booking reference and matching email, when I request an available new time, then my rescheduling request is recorded and the original appointment remains unchanged until staff approval.
- Given the requested new time is already booked, when I submit a rescheduling request, then the system rejects that time and asks me to select another available time.
## US-08 — View Staff Calendar
Priority: Must

As a salon staff member, I want to view appointments in a calendar so that I can organize the salon schedule.

- Given appointments exist for a selected date, when I open the staff calendar, then I see the scheduled appointments and their statuses.
- Given no appointments exist for that date, when I open the calendar, then I see an empty-schedule message.

## US-09 — Confirm Appointment
Priority: Must

As a salon staff member, I want to confirm pending appointment requests so that clients know their bookings are accepted.

- Given a pending appointment request has an available time, when authorized staff confirm it, then the appointment status changes to Confirmed.
- Given a pending appointment request has a time that is no longer available, when staff attempt to confirm it, then the system prevents confirmation and displays a scheduling conflict message.
## US-10 — Update Service Details
Priority: Could

As a salon staff member, I want to update a service's price and duration so that clients see accurate booking information.

- Given I am an authorized staff member and enter a service price greater than zero and a duration of at least 15 minutes, when I save the changes, then the updated price and duration appear in the services list.
- Given I enter a price of zero or less or a duration below 15 minutes, when I attempt to save the service, then the system rejects the changes and displays a validation message.

## Priority Summary
- Must: US-01, US-02, US-04, US-05, US-08, US-09
- Should: US-03, US-06, US-07
- Could: US-10
## AI Review Log

**Review prompt:** Here are my user stories for a Flask prototype. Check each one against INVEST and tell me which are too big, vague or not testable. Do not rewrite them; list problems only.

**Copilot feedback and decisions:**
- US-03: Accepted. Clarified stylist availability and what happens when no stylist is available.
- US-04: Accepted. Added specific contact information validation rules.
- US-05: Accepted. Defined appointment lookup using a booking reference and matching email.
- US-06: Accepted. Defined cancellation request status and invalid cancellation cases.
- US-07: Accepted. Clarified that the original appointment stays unchanged until staff approval.
- US-09: Accepted. Added handling for a scheduling conflict during confirmation.
- US-10: Accepted. Defined valid service prices and durations.
- General feedback: Rejected splitting every story solely because it depends on another booking step. The stories remain small and independently testable at the acceptance-criteria level.

**Reflection:** Copilot helped identify missing rules and edge cases. I reviewed the suggestions and revised the acceptance criteria to make the expected behavior clearer and easier to test.## Assignment Reflection Questions

### 1. Which story did you split into smaller stories, and why?

I did not split any of my existing stories during this review. Copilot found that some stories depended on earlier booking steps, but none was clearly too large. I kept the stories separate and improved their acceptance criteria so each one describes a specific, testable outcome.

### 2. Which story was hardest to write acceptance criteria for? What made it hard?

US-05 — View My Appointments was the hardest because I needed to decide how clients could find their appointments without creating a full login system. I chose to use a booking reference and matching email address. This makes appointment lookup easier to test while helping protect clients' personal information.