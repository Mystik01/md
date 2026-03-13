content = r"""Good idea starting Activity B early. The design document is where you usually gain a lot of marks because you can show technical thinking and system design. The key difference from Activity A:

- Activity A (Proposal) → explain what you will build and why
- Activity B (Design) → explain exactly how the system will work

Your design document should therefore be more technical and more diagram-heavy.

Below is a recommended structure that aligns well with how these assessments are usually marked.

---

# Activity B – Design Document Structure

---

## 1 System Overview

### 1.1 System Purpose

Explain:
- what the system does
- the main users of the system
- what problems the system solves
- how the platform supports both customers and producers

Keep this short (about half a page).

---

### 1.2 Key System Features

Briefly list the major features that will be implemented:

Examples:
- online storefront
- product browsing
- ordering system
- customer account dashboard
- loyalty system
- order tracking
- producer dashboard
- stock management

Explain what each feature allows users to do.

---

## 2 System Architecture

This section explains the technical structure of the system.

---

### 2.1 Overall System Architecture

Explain the architecture chosen (likely 3-tier architecture).

Describe:
- presentation layer
- application layer
- data layer
- how these layers interact

**Diagram 1 – System Architecture Diagram**

Should look like stacked layers:

```
Presentation Layer
(Web Interface)

Application Layer
(Business Logic)

Data Layer
(Database)
```

---

### 2.2 Technology Stack

Explain what technologies will be used.

Examples:

Frontend:
- TypeScript
- React / Next.js
- HTML
- CSS

Backend:
- Node.js
- API routes
- server-side logic

Database:
- SQL or NoSQL database

Explain why these technologies are appropriate.

---

## 3 Data Design

This section shows how data will be structured and stored.

---

### 3.1 Entity Relationship Diagram (ERD)

This is one of the most important diagrams.

Entities might include:
- Users
- Products
- Orders
- Producers
- LoyaltyPoints
- OrderItems

**Diagram 2 – Entity Relationship Diagram**

Example structure:

```
Users
│
├ userID
├ name
├ email
├ password

Products
│
├ productID
├ name
├ price
├ producerID

Orders
│
├ orderID
├ userID
├ orderDate
├ status
```

Relationships:
- Users place Orders
- Orders contain Products
- Producers supply Products

---

### 3.2 Data Dictionary

For each table describe:
- field name
- data type
- purpose

Example:

- UserID – integer – unique identifier
- Email – string – user login email
- Password – hashed string – stored securely

---

## 4 User Interface Design

This section includes wireframes for key pages.

You should create simple UI mockups.

---

### 4.1 Website Navigation Structure

Include:

**Diagram 3 – Site Map**

Same structure you used in Activity A but possibly slightly expanded.

---

### 4.2 Wireframes

Create simple wireframe layouts.

Include:

**Diagram 4 – Homepage Wireframe**

Should show:
- navigation bar
- featured products
- search bar
- login/register

---

**Diagram 5 – Product Page Wireframe**

Should include:
- product image
- product description
- price
- add to basket button

---

**Diagram 6 – Customer Dashboard Wireframe**

Should include:
- order history
- loyalty points
- account settings
- order tracking

---

**Diagram 7 – Producer Dashboard Wireframe**

Should include:
- product list
- add product button
- edit product option
- stock quantity input

---

## 5 Process Design

This section shows how key processes work step-by-step.

---

### 5.1 Ordering Process

**Diagram 8 – Sequence Diagram (Order Process)**

Example flow:

Customer → Website
Website → Server
Server → Database
Database → Server
Server → Website
Website → Customer

Steps include:
- selecting products
- adding to basket
- checkout
- order confirmation
- stock update

---

### 5.2 Stock Update Process

Explain:
- how stock changes when orders occur
- how producers update stock manually

**Diagram 9 – Flowchart (Stock Update)**

Example:

```
Order placed
↓
Check stock
↓
Reduce stock quantity
↓
Update database
```

---

## 6 Security Design

Explain how the system will remain secure.

Topics to cover:
- password hashing
- secure authentication
- input validation
- preventing SQL injection
- secure session handling

---

## 7 Accessibility Design

Explain how accessibility will be implemented.

Examples:
- screen reader compatibility
- keyboard navigation
- colour contrast
- alternative text for images
- responsive design

---

## 8 Testing Strategy

Explain how the system will be tested.

Types of testing:
- unit testing
- integration testing
- usability testing
- accessibility testing

Include examples of tests.

---

## Recommended Diagrams for Activity B

These diagrams usually give the most marks.

| Diagram | Purpose |
|---------|---------|
| System Architecture Diagram | overall system structure |
| Entity Relationship Diagram | database design |
| Site Map | page navigation |
| Wireframes (4+) | UI layout |
| Sequence Diagram | system interactions |
| Flowchart | system processes |

Typical total: 8–10 diagrams

---

## Typical Design Document Length

Most strong submissions are around:

15–30 pages

depending on diagrams and explanations.

---

## Quick Tip

Your wireframes are where you can gain easy marks because they clearly show:
- UI thinking
- user experience
- system functionality

Even simple Figma wireframes work perfectly.

---

If you want, I can also show you the exact 9 diagrams that almost every distinction-level design document contains, which makes the design document much easier to complete quickly.
"""

with open('/Users/logan/Desktop/md/d2.md', 'w') as f:
    f.write(content)
