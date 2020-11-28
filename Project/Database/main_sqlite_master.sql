INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'subject', 'subject', 2, 'CREATE TABLE subject(
   subject_id INTEGER PRIMARY KEY,
   subject_name TEXT
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'shedule', 'shedule', 3, 'CREATE TABLE shedule(
    lesson_id INTEGER PRIMARY KEY,
    subject_id INTEGER,
    week_day TEXT,
    time TEXT,
    FOREIGN KEY(subject_id) REFERENCES subject(subject_id) ON DELETE CASCADE
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'school_tasks', 'school_tasks', 4, 'CREATE TABLE school_tasks(
    task_id INTEGER PRIMARY KEY,
    subject_id INTEGER,
    deadline TEXT,
    week_day TEXT,
    task TEXT,
    FOREIGN KEY(subject_id) REFERENCES subject(subject_id) ON DELETE CASCADE
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'school_event', 'school_event', 5, 'CREATE TABLE school_event(
    event_id INTEGER PRIMARY KEY,
    event TEXT,
    subject_id INTEGER,
    date TEXT,
    week_day TEXT,
    time TEXT,
    FOREIGN KEY(subject_id) REFERENCES subject(subject_id) ON DELETE CASCADE
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'daily_tasks', 'daily_tasks', 6, 'CREATE TABLE daily_tasks(
    task_id INTEGER PRIMARY KEY,
    task TEXT,
    important INTEGER,
    class TEXT,
    deadline TEXT
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'my_event', 'my_event', 7, 'CREATE TABLE my_event(
    event_id INTEGER PRIMARY KEY,
    event TEXT,
    date TEXT,
    time TEXT
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'big_tasks', 'big_tasks', 8, 'CREATE TABLE big_tasks(
    task_id INTEGER PRIMARY KEY,
    task TEXT,
    important INTEGER,
    class TEXT,
    deadline TEXT
)');