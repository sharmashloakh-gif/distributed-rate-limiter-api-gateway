CREATE DATABASE IF NOT EXISTS sentinel_gate;
USE sentinel_gate;

CREATE TABLE api_clients (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(120) NOT NULL,
    api_key_hash CHAR(64) NOT NULL UNIQUE,
    tier ENUM('FREE', 'PRO', 'ENTERPRISE') DEFAULT 'FREE',
    rpm_limit INT NOT NULL DEFAULT 60,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE request_audit_logs (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    client_id BIGINT NOT NULL,
    endpoint VARCHAR(255) NOT NULL,
    status_code SMALLINT NOT NULL,
    latency_ms INT NOT NULL,
    requested_at TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP(3),
    INDEX idx_client_time (client_id, requested_at),
    FOREIGN KEY (client_id) REFERENCES api_clients(id)
);
