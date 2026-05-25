use('taller_mongo_2026');

// Devuelve todas las empleadas de la empresa usando $match

db.employees.aggregate([
    { $match: { gender: "female" } }
]); 