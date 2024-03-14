

# Django based  Library Management

## Navigate to the project directory:

```bash
  cd Django-librarymanagement
```
## 3 . Create a virtual environment:
```bash
  python3 -m venv env
```
## 4. Activate the virtual environment:
```bash
  source env/bin/activate
```
## 5. Install the project dependencies:
```bash
  pip install -r requirements.txt
```
## 6 . Run the server
```bash
  python manage.py runserver
```
## 7 . Go to localhost:8000
---

##### Admin can

1.  login to admin dashboard
2.  check all issues :

    - see issues ,
    - delete issues ,
    - search issues by studentid
    - filter issues based on :

      - issued or not,
      - returned or not ,

3.  accept a issue :

    - from the dashboard where admin has to manually select return date
      **or**
    - from the Issue requests page where return date is automatically calculated

4.  add , delete search books and filter books based on author
5.  add , delete , search author
6.  calculate fine by clicking a button ,
7.  create, delete fine ,search fines for studentid
8.  toggle fine paid status (if paid in cash)
9.  search ,modify,add,delete students , filter them based on department and check all fines and issues of that student
10. can see the last-login , date joined & the student associated to a particular user
11. can change password for any user
