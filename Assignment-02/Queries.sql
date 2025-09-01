--4. Create Vendor Table:

CREATE TABLE SubscriptionPlan (
    SubscriptionPlanID INT PRIMARY KEY,
    PlanName VARCHAR(100) NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    Duration INT NOT NULL, -- duration in months
    Features TEXT
);

CREATE TABLE Vendor (
    VendorID INT PRIMARY KEY AUTO_INCREMENT,
    BusinessName VARCHAR(255) NOT NULL,
    ContactPerson VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(20),
    BusinessAddress TEXT,
    SubscriptionPlanID INT,
    FOREIGN KEY (SubscriptionPlanID) REFERENCES SubscriptionPlan(SubscriptionPlanID)
);

--5. Create ProductCategory Table (M:N)

CREATE TABLE ProductCategory (
    ProductID INT NOT NULL,
    CategoryID INT NOT NULL,
    PRIMARY KEY (ProductID, CategoryID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
);

--6. Insert new vendor "SmartTech Ltd." under Basic plan

INSERT INTO Vendor (BusinessName, ContactPerson, Email, PhoneNumber, BusinessAddress, SubscriptionPlanID)
VALUES ('SmartTech Ltd.', 'Rahim Khan', 'rahim@smarttech.com', '017XXXXXXXX', 'Dhaka, Bangladesh', 1);

--7. Insert product "Laptop" under Electronics category

INSERT INTO Product (VendorID, ProductName, Description, Price, StockQuantity, Status)
VALUES (1, 'Laptop', 'High performance laptop', 75000, 10, 'active');


--8. Update stock quantity of "Laptop" to 15

UPDATE Product
SET StockQuantity = 15
WHERE ProductName = 'Laptop' AND VendorID = 1;

--9. Delete customer with email "oldcustomer@gmail.com"

DELETE FROM Customer
WHERE Email = 'oldcustomer@gmail.com';

--10. Display all vendors with subscription plan name and price

SELECT v.BusinessName, sp.PlanName, sp.Price
FROM Vendor v
JOIN SubscriptionPlan sp ON v.SubscriptionPlanID = sp.SubscriptionPlanID;

--11. Find all products under "Electronics" category with name, price, stock

SELECT p.ProductName, p.Price, p.StockQuantity
FROM Product p
JOIN ProductCategory pc ON p.ProductID = pc.ProductID
JOIN Category c ON pc.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Electronics';

--12. List all orders placed by customer "Karim Uddin"

SELECT o.OrderID, o.OrderDate, o.TotalAmount, o.OrderStatus
FROM Order o
JOIN Customer c ON o.CustomerID = c.CustomerID
WHERE c.Name = 'Karim Uddin';

--13. Show payment details for order_id = 1

SELECT Method, Amount, PaymentStatus
FROM Payment
WHERE OrderID = 1;

--14. Top 5 best-selling products by total quantity sold

SELECT p.ProductName, SUM(oi.Quantity) AS TotalSold
FROM OrderItem oi
JOIN Product p ON oi.ProductID = p.ProductID
GROUP BY p.ProductID, p.ProductName
ORDER BY TotalSold DESC
LIMIT 5;

--15. Total sales amount per vendor

SELECT v.BusinessName, SUM(oi.Subtotal) AS TotalSales
FROM Vendor v
JOIN Product p ON v.VendorID = p.VendorID
JOIN OrderItem oi ON p.ProductID = oi.ProductID
GROUP BY v.VendorID, v.BusinessName;

--16. Customers who have not placed any orders

SELECT c.Name, c.Email
FROM Customer c
LEFT JOIN Order o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;

--17. Total number of active products on the platform

SELECT COUNT(*) AS ActiveProductCount
FROM Product
WHERE Status = 'active';

--18. Vendors subscribed to the Enterprise plan

SELECT v.BusinessName, v.ContactPerson, v.Email
FROM Vendor v
JOIN SubscriptionPlan sp ON v.SubscriptionPlanID = sp.SubscriptionPlanID
WHERE sp.PlanName = 'Enterprise';

--19. Average order amount per customer

SELECT c.Name, AVG(o.TotalAmount) AS AvgOrderAmount
FROM Customer c
JOIN Order o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.Name;

--20. Customers who purchased products from more than one vendor

SELECT c.Name, c.Email
FROM Customer c
JOIN Order o ON c.CustomerID = o.CustomerID
JOIN OrderItem oi ON o.OrderID = oi.OrderID
JOIN Product p ON oi.ProductID = p.ProductID
GROUP BY c.CustomerID, c.Name, c.Email
HAVING COUNT(DISTINCT p.VendorID) > 1;



