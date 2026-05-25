use('taller_mongo_2026');
// 1- Mostrar todos los documentos de la colección restaurantes

// db.restaurantes.find()*/

// 2- Mostrar los campos restaurant_id, nombre, distrito y cocina, pero excluya el campo _id para todos los documentos de la colección restaurantes

//db.restaurantes.find({}, { restaurant_id: 1, name: 1, borough: 1, cuisine:1, _id: 0 })*/

// 3- Mostrar los primeros 5 restaurantes que se encuentran en el distrito Bronx

// db.restaurantes.find({borough: 'Bronx'}).limit(5)*/

// 4- Devolver los restaurantes que lograron una puntuación superior a 80 pero inferior
//  a 100

// db.restaurantes.find({ grades: { $elemMatch: { score: { $gt: 80, $lt: 100 } } } })


// 5- Devolver los restaurantes que se ubican en un valor de latitud inferior a -95.754168

// db.restaurantes.find({ "address.coord.1": { $lt: -95.754168 } })

// 6- Devolver los restaurantes que no preparan cocina americana y lograron una puntuación 
// superior a 70 y se ubicaron en una longitud inferior a -65.754168. Nota: Realice 
// esta consulta sin usar el operador $and

// db.restaurantes.find({   cuisine: { $ne: "American" }, "grades.score": { $gt: 70 }, "address.coord.0": { $lt: -65.754168 }})

// 7- Devolver los restaurantes que no preparan cocina americana y lograron un punto de 
// calificación 'A' que no pertenece al distrito de Brooklyn. El documento debe mostrarse 
// según la cocina en orden descendente

// db.restaurantes.find({ cuisine: { $ne: "American" }, "grades.grade": "A", borough: { $ne: "Brooklyn" }}).sort({ cuisine: -1 })

// 8- Devolver los restaurantes que pertenecen al distrito Bronx y preparan platos 
// americanos o chinos

// db.restaurantes.find({ borough: "Bronx", $or: [{ cuisine: "American" }, { cuisine: "Chinese" }]})

// 9- Devolver ID del restaurante, nombre, distrito y la cocina para aquellos restaurantes 
// que pertenecen al distrito de Staten Island o Queens o Bronx o Brooklyn

// db.restaurantes.find({ borough: { $in: ["Staten Island", "Queens", "Bronx", "Brooklyn"] } }, { restaurant_id: 1, name: 1, borough: 1, cuisine: 1, _id: 0 })

// 10- Devolver ID del restaurante, nombre, distrito y la cocina de aquellos restaurantes que lograron una puntuación que no supere los 10

// db.restaurantes.find({ "grades.score": { $lte: 10 } }, { restaurant_id: 1, name: 1, borough: 1, cuisine: 1, _id: 0 })

// 11- Devolver ID del restaurante, el nombre y las calificaciones del restaurante para aquellos restaurantes que obtuvieron una calificación de "A" y obtuvieron un puntaje de 11 en una fecha ISO "2014-08-11T00: 00: 00Z" entre muchas fechas de encuesta

// db.restaurantes.find({ grades: { $elemMatch: { grade: "A", score: 11, date: ISODate("2014-08-11T00:00:00Z") } } }, { restaurant_id: 1, name: 1, grades: 1, _id: 0 } )

// 12- Devolver ID del restaurante, nombre, dirección y ubicación geográfica del restaurante de aquellos donde el segundo elemento de la matriz coord contiene un valor que es más de 42 y hasta 52

// db.restaurantes.find( { "address.coord.1": { $gt: 42, $lte: 52 } }, { restaurant_id: 1, name: 1, address: 1, _id: 0 } )

// 13- Crea un par de restaurantes que te gusten. Tendrás que buscar en Google Maps los datos de las coordenadas

/* db.restaurantes.insertMany([
  {
    name: "Bar Nestor",
    borough: "San Sebastián",
    cuisine: "Spanish",
    address: {
      street: "Calle Pescadería, 11",
      city: "San Sebastián",
      coord: [-1.9769, 43.3223]
    },
    grades: [{ date: ISODate("2024-01-01T00:00:00Z"), grade: "A", score: 15 }]
  },
  {
    name: "Asador Etxebarri",
    borough: "Atxondo",
    cuisine: "Basque",
    address: {
      street: "Plaza San Juan, 1",
      city: "Atxondo",
      coord: [-2.6171, 43.1342]
    },
    grades: [{ date: ISODate("2024-01-01T00:00:00Z"), grade: "A", score: 20 }]
  }
]) */

// 14- Actualiza los restaurantes. Cambia el tipo de cocina 'Ice Cream, Gelato, Yogurt, Ices' por 'sweets'

// db.restaurantes.updateMany( { cuisine: "Ice Cream, Gelato, Yogurt, Ices" }, { $set: { cuisine: "sweets" } })

// 15- Actualiza nombre del restaurante 'Wild Asia' por 'Wild Wild West'

// db.restaurantes.updateOne( { name: "Wild Asia" }, { $set: { name: "Wild Wild West" } } )

// 16- Borra los restaurantes con latitud menor que -95.754168

// db.restaurantes.deleteMany({ "address.coord.0": { $lt: -95.754168 } })

// 17- Borra los restaurantes cuyo nombre empiece por 'C'

// db.restaurantes.deleteMany({ name: /^C/ })