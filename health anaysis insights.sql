-- 1. Total patients
SELECT COUNT(*) AS total_patients
FROM health_data;


-- 2. Gender distribution
SELECT gender, COUNT(*) AS total
FROM health_data
GROUP BY gender;


-- 3. Average age by gender
SELECT gender, AVG(age) AS avg_age
FROM health_data
GROUP BY gender;


-- 4. Most common disease
SELECT disease, COUNT(*) AS total
FROM health_data
GROUP BY disease
ORDER BY total DESC
LIMIT 1;


-- 5. Patients per city
SELECT city, COUNT(*) AS total_patients
FROM health_data
GROUP BY city;


-- 6. Average treatment cost by city
SELECT city, AVG(treatment_cost) AS avg_cost
FROM health_data
GROUP BY city;


-- 7. Year-wise patient visits
SELECT YEAR(visit_date) AS year, COUNT(*) AS total_visits
FROM health_data
GROUP BY year;


-- 8. Patients handled per doctor
SELECT doctor, COUNT(*) AS total_patients
FROM health_data
GROUP BY doctor;


-- 9. Most expensive disease
SELECT disease, AVG(treatment_cost) AS avg_cost
FROM health_data
GROUP BY disease
ORDER BY avg_cost DESC
LIMIT 1;


-- 10. City-wise disease distribution
SELECT city, disease, COUNT(*) AS total
FROM health_data
GROUP BY city, disease
ORDER BY city;


-- 11. High-risk patients (BP > 140 or Sugar > 150)
SELECT *
FROM health_data
WHERE bp > 140 OR sugar_level > 150;


-- 12. BMI vs disease (avg BMI per disease)
SELECT disease, AVG(bmi) AS avg_bmi
FROM health_data
GROUP BY disease;


-- 13. Age group analysis
SELECT 
  CASE 
    WHEN age < 25 THEN 'Young'
    WHEN age BETWEEN 25 AND 40 THEN 'Adult'
    ELSE 'Senior'
  END AS age_group,
  COUNT(*) AS total
FROM health_data
GROUP BY age_group;


-- 14. Top 3 doctors with highest workload
SELECT doctor, COUNT(*) AS total_patients
FROM health_data
GROUP BY doctor
ORDER BY total_patients DESC
LIMIT 3;


-- 15. Running total of patients over time
SELECT 
  visit_date,
  COUNT(*) OVER (ORDER BY visit_date) AS running_total
FROM health_data;

















