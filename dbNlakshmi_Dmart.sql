-- MySQL-compatible version of dmart_backup.sql
-- Converted from SQLite format

SET FOREIGN_KEY_CHECKS = 0;

CREATE DATABASE IF NOT EXISTS dbNlakshmi_Dmart;
USE dbNlakshmi_Dmart;

-- ------------------------------
-- Table: Cashier
-- ------------------------------
CREATE TABLE Cashier (
  CashierID VARCHAR(20) PRIMARY KEY,
  CashierName VARCHAR(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO Cashier (CashierID, CashierName) VALUES
('C003','Vijay'),
('C033','Vinod'),
('C520','Sita'),
('C201','John'),
('C4055','Xavier'),
('C9050','Wasim'),
('C00034','Maya'),
('C60238','Anand'),
('C7578','Uday'),
('C0770','David');

-- ------------------------------
-- Table: Supplier
-- ------------------------------
CREATE TABLE Supplier (
  SupplierID VARCHAR(20) PRIMARY KEY,
  SupplierName VARCHAR(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO Supplier (SupplierID, SupplierName) VALUES
('S342','Bindu'),
('S6633','Mahesh'),
('S0213','Jahnavi'),
('S1377','Kiran'),
('S712','Govind'),
('S224','Trisha'),
('S310','Latha'),
('S2160','Pavan'),
('S0324','Ishanth'),
('S274','Jaswanth');

-- ------------------------------
-- Table: Customer
-- ------------------------------
CREATE TABLE Customer (
  CustomerID VARCHAR(20) PRIMARY KEY,
  CustomerName VARCHAR(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO Customer (CustomerID, CustomerName) VALUES
('C3001','Hari'),
('C743','Rita'),
('C313','Gowri'),
('C0021','Eswar'),
('C5320','Yash'),
('C0981','Philip'),
('C0913','Satish'),
('C3014','Sahithya'),
('C0473','Mounika');

-- ------------------------------
-- Table: Item
-- ------------------------------
CREATE TABLE Item (
  ItemID VARCHAR(20) PRIMARY KEY,
  Description VARCHAR(100) NOT NULL,
  UnitPrice INT,
  StockQty INT DEFAULT 0 CHECK (StockQty > 0),
  SupplierID VARCHAR(20),
  FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO Item (ItemID, Description, UnitPrice, StockQty, SupplierID) VALUES
('I0413','Purse',700,30,'S342'),
('I1373','Shirt',350,57,'S310'),
('I3103','Pen',10,230,'S712'),
('I5234','Bag',1000,164,'S2160'),
('I4140','Bottle',200,44,'S712'),
('I684','Plate',120,80,'S2160'),
('I7309','Perfume',50,1,'S2160'),
('I0019','Book',90,79,'S1377'),
('I0901','SweetBox',210,21,'S274'),
('I5335','OilPaints',160,59,'S342');

-- ------------------------------
-- Table: BillHeader
-- ------------------------------
CREATE TABLE BillHeader (
  BillNumber VARCHAR(20) PRIMARY KEY,
  BillDate DATE,
  CashierID VARCHAR(20),
  CustomerID VARCHAR(20),
  FOREIGN KEY (CashierID) REFERENCES Cashier(CashierID),
  FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO BillHeader (BillNumber, BillDate, CashierID, CustomerID) VALUES
('B245','2025-11-03','C003','C0981'),
('B310','2021-01-31','C7578','C3014'),
('B833','2025-11-10','C60238','C3014'),
('B756','2025-11-10','C4055','C743'),
('B922','2024-09-11','C7578','C743'),
('B534','2023-05-31','C9050','C3001'),
('B331','2024-09-04','C520','C0981'),
('B004','2021-01-16','C003','C0021'),
('B144','2024-05-04','C201','C5320'),
('B032','2022-12-14','C00034','C0021'); 

-- ------------------------------
-- Table: BillDetail
-- ------------------------------
CREATE TABLE BillDetail (
  BillNumber VARCHAR(20),
  ItemID VARCHAR(20),
  SolQty INT DEFAULT 1,
  PRIMARY KEY (BillNumber, ItemID),
  FOREIGN KEY (BillNumber) REFERENCES BillHeader(BillNumber),
  FOREIGN KEY (ItemID) REFERENCES Item(ItemID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO BillDetail (BillNumber, ItemID, SolQty) VALUES
('B144','I0019',15),
('B144','I3103',20),
('B756','I0413',1),
('B922','I0901',3),
('B833','I4140',5),
('B310','I5234',1),
('B310','I3103',15),
('B534','I684',5),
('B032','I4140',2),
('B245','I7309',4); 

SET FOREIGN_KEY_CHECKS = 1;
