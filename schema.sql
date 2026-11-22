PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'customer'
);

CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price_cents INTEGER NOT NULL,
    duration_minutes INTEGER NOT NULL,
    active INTEGER DEFAULT 1
);

CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    client_name TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);

INSERT INTO users (id, username, password_hash, role) VALUES
    (1, 'maya_patel', 'sample_hash_1', 'customer'),
    (2, 'jordan_lee', 'sample_hash_2', 'customer'),
    (3, 'sofia_garcia', 'sample_hash_3', 'customer');

INSERT INTO services (id, name, category, price_cents, duration_minutes, active) VALUES
    (1, 'Haircut', 'Hair', 3500, 45, 1),
    (2, 'Hair Coloring', 'Hair', 9000, 120, 1),
    (3, 'Hair Styling', 'Styling', 5000, 60, 1),
    (4, 'Hair Wash', 'Hair Care', 2000, 30, 1),
    (5, 'Deep Conditioning', 'Treatment', 4500, 45, 1),
    (6, 'Blow Dry', 'Styling', 3000, 30, 1);

INSERT INTO appointments
    (id, user_id, service_id, client_name, date, time, status, notes)
VALUES
    (1, 1, 1, 'Maya Patel', '2026-11-18', '10:00', 'pending', NULL),
    (2, 2, 3, 'Jordan Lee', '2026-11-18', '11:30', 'confirmed', NULL),
    (3, 3, 2, 'Sofia Garcia', '2026-11-18', '14:00', 'confirmed', NULL);