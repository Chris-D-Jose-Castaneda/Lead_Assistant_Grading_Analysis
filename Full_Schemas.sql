USE class_grades;



-- Section I: Delete null values

-- If you hit “safe‐update mode” errors, disable it for this session:
SET SQL_SAFE_UPDATES = 0;

-- Delete any rows where SIS User ID is NULL or blank
DELETE FROM spring2023_final
 WHERE `SIS User ID` IS NULL
    OR TRIM(`SIS User ID`) = '';

-- Re-enable safe updates
SET SQL_SAFE_UPDATES = 1;

-- Verify that no such rows remain
SELECT COUNT(*) AS null_sis_count
  FROM spring2023_final
 WHERE `SIS User ID` IS NULL;



-- Section II: Create new column & set to primary Key

ALTER TABLE spring2023_final
  ADD COLUMN `Student #` INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;



-- Section III: Replace Section w/ Respective Name [FA23,FA24,SP23,SP24,SP25]

-- If you hit safe‐update mode errors, disable it for this session
SET SQL_SAFE_UPDATES = 0;

-- Update all rows
UPDATE spring2023_final
   SET `Section` = 'SP23';

-- Re‐enable safe‐updates
SET SQL_SAFE_UPDATES = 1;


-- Section IV: Drop Duplicate Cols/Confidential data

ALTER TABLE `class_grades`.`fall2024_final` 
DROP COLUMN `Unposted Final Score`,
DROP COLUMN `Unposted Current Score`,
DROP COLUMN `Current Score`,
DROP COLUMN `Final Points`,
DROP COLUMN `Current Points`,
DROP COLUMN `Assignments Unposted Final Score`,
DROP COLUMN `Assignments Final Score`,
DROP COLUMN `Assignments Unposted Current Score`,
DROP COLUMN `Assignments Current Score`,
DROP COLUMN `Assignments Final Points`,
DROP COLUMN `Assignments Current Points`,
DROP COLUMN `SIS Login ID`,
DROP COLUMN `SIS User ID`,
DROP COLUMN `ID`,
DROP COLUMN `Student`;
