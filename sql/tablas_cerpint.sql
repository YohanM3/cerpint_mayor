CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    brand VARCHAR(50),
    supplier VARCHAR(100),
    sale_price DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE municipalities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
); 
CREATE TABLE customers (
  rif VARCHAR(20) PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  address VARCHAR(100) NOT NULL,
  state_name VARCHAR(50) NOT NULL,
  municipality_id INT not null,
  advisor_cedula VARCHAR(15),
  FOREIGN KEY (advisor_cedula) REFERENCES sales_advisors(cedula)
);

CREATE TABLE sales_advisors (
cedula VARCHAR(10) NOT NULL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
address VARCHAR(100) NOT NULL,
number_phone VARCHAR(13) NOT NULL
);

CREATE TABLE sales (
  id INT AUTO_INCREMENT PRIMARY KEY,
  advisor_cedula VARCHAR(10),
  customer_rif VARCHAR(20),
  total DECIMAL(10,2),
  FOREIGN KEY(advisor_cedula) REFERENCES sales_advisors(cedula),
  FOREIGN KEY(customer_rif) REFERENCES customers(rif)
)