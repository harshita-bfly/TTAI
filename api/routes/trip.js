const router=require("express").Router()
const Trip=require("../models/Trip");
const moment=require("moment")
//GET
router.get("/recent",async(req,res)=>{
  const email = req.query.email;
  try {
      const currentDate = new Date();
      const trips = await Trip.aggregate([
          {
              $match: { email: email, startDate: { $lt: currentDate } } // Match trips with start date before current date
          },
          {
              $sort: { startDate: -1 } // Sort trips by start date in descending order
          },
          {
              $limit: 1 // Limit to the first trip, which is the latest trip before the current date
          }
      ]);
      console.log(trips);
      res.status(200).json(trips[0].photo);
  } catch (err) {
      console.error('Error fetching trip dates:', err);
      res.status(500).json({ error: 'Internal Server Error' });
  }
})

router.post('/', async (req, res) => {
    console.log("hi")
    const { userId, email, photo,startDate } = req.body;

    const formattedDate = moment(startDate, 'DD-MM-YYYY').toDate();
    try {
      // Create a new trip instance
      const trip = new Trip({
        userId,
        email,
        photo,
        startDate:formattedDate
      });
  
      // Save the trip to the database
      await trip.save();
  
      // Respond with the saved trip
      res.status(201).json(trip);
    } catch (err) {
      console.error(err.message);
      res.status(500).send('Server Error');
    }
  });
  
  router.get('/dates', async (req, res) => {
    const email=req.query.email;
    try {
      const trips=await Trip.aggregate([
        {
            $match:{email:email}
        }
    ])
        res.status(200).json(trips);
    } catch (err) {
        console.error('Error fetching trip dates:', err);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});
  


module.exports=router