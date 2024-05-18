import React, { useEffect, useState } from 'react';
import axios from 'axios';
import moment from 'moment';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import './Upcoming.css';

const Upcoming = () => {
    const [tripImage, setTripImage] = useState(null);
    const [tripDates, setTripDates] = useState([]);
    const [selectedDate, setSelectedDate] = useState(new Date());

    useEffect(() => {
        const fetchTripImage = async () => {
            try {
                const response = await axios.get('/trip/recent', {
                    headers: { 'Content-Type': 'application/json' },
                    params: { email: 'Khushi123@gmail.com' }
                });

                if (response.status === 200) {
                    setTripImage(response.data);
                } else {
                    console.error('Error fetching trip image:', response.statusText);
                }
            } catch (error) {
                console.error('Error fetching trip image:', error);
            }
        };

        const fetchTripDates = async () => {
            try {
                const response = await axios.get('/trip/dates', {
                    headers: { 'Content-Type': 'application/json' },
                    params: { email: 'Khushi123@gmail.com' }
                });

                if (response.status === 200) {
                    setTripDates(response.data);
                } else {
                    console.error('Error fetching trip dates:', response.statusText);
                }
            } catch (error) {
                console.error('Error fetching trip dates:', error);
            }
        };

        fetchTripImage();
        fetchTripDates();
    }, []);

    const tileClassName = ({ date, view }) => {
        if (view === 'month') {
            const currentDate = new Date();
            const formattedDate = moment(date).format('YYYY-MM-DD'); // Changed date format
            const tripDate = tripDates.find(x => {
                const tripFormattedDate = moment(x.startDate).format('YYYY-MM-DD'); // Changed date format
                return tripFormattedDate === formattedDate && moment(x.startDate).isBefore(currentDate);
            });
    
            if (tripDate) {
                return 'highlighted_item'; // Use a generic class name
            }
        }
        return '';
    };
    

    return (
        <div className="upcoming">
            <span className="upcomingtrip">Upcoming Trip</span>
            <div className="availablejourney">
                <span className="all">Upcoming</span>
            </div>
            {tripImage && <img src={tripImage} className="Tripimg" alt="Trip" />}
            <Calendar
                view='month'
                onChange={setSelectedDate}
                value={selectedDate}
                tileClassName={tileClassName}
            />
        </div>
    );
};

export default Upcoming;
