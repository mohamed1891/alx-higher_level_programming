-- Switching to the hbtn_0c_0 database
USE `hbtn_0c_0`;

-- Altering the first_table to convert to utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
