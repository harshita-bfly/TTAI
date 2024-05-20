import React, { useState } from 'react'
import './Question.css'
function Question() {
    const [theme, setTheme] = useState('')
    const [type, setType] = useState('')
    const [loc, setLoc] = useState('')
    const [quesNo, setQuesNo] = useState(1);


    const questions = {
        1: {
            ques: 'What theme would you prefer?',
            options: ['Family', 'Adventure', 'Peace', 'Romantic']
        },
        2: {
            ques: 'What kind of place are you looking for?',
            options: ['Mountains', 'Beaches', 'Historical Places', 'Deserts']
        },
        3: {
            ques: 'Choose a place you would like to visit',
            options: (type) => {
                switch (type) {
                    case 'Mountains':
                        return ['Kashmir', 'Manali', 'Nainital', 'Kasauli'];
                    case 'Beaches':
                        return ['Goa', 'Andaman & Nicobar', 'Kerala', 'Lakshadweep'];
                    case 'Historical Places':
                        return ['Lucknow', 'Delhi', 'Jaipur', 'Tamil Nadu']
                    case 'Deserts':
                        return ['Rajasthan', 'Gujarat', 'Ladakh', 'Himachal']
                    default:
                        return []
                }
            }
        }
    }

    const handleOption = (option) => {
        if (quesNo === 1) {
            setTheme(option)
            setQuesNo(2);

        } else if (quesNo === 2) {
            setType(option)
            setQuesNo(3)
        } else {
            setLoc(option)
        }
    }

    const bgImg = [ 
        'url(https://akm-img-a-in.tosshub.com/businesstoday/images/story/202305/howrah_bridge_1-sixteen_nine.jpg?size=1200:675)',
        'url(https://travellerhunt.com/wp-content/uploads/2020/10/63-Best-Tourist-Places-To-Visit-In-India-For-A-Perfect-Holiday-In-2020.jpg)'
    ]

    const typeBgImg = {
        'Mountains': 'url(https://img.freepik.com/free-photo/beautiful-shot-small-village-surrounded-by-lake-snowy-hills_181624-37802.jpg?t=st=1716200250~exp=1716203850~hmac=9897882360ad50c48b2aa84f08f67fa999addf039e425a372869708e7289b2b7&w=900)',
        'Beaches': 'url(https://img.freepik.com/free-photo/swimming-pool_74190-2104.jpg?t=st=1716200480~exp=1716204080~hmac=6cc886423ea817ce06cd7572199e492df80a9aa741d3f2fde14ee62fac82845a&w=900)',
        'Historical Places': 'url(https://www.oyorooms.com/blog/wp-content/uploads/2017/12/Feature-Image-2.jpg)',
        'Deserts': 'url(https://img.freepik.com/free-photo/group-people-camels-desert_181624-59627.jpg?t=st=1716200525~exp=1716204125~hmac=df2380e7e6ee1e6a040c2813edc0758272afbc4283a7320ddb2493ddf2964866&w=900)'
    }
    const curQuesData = questions[quesNo]
    // console.log(curQuesData)
    const options = quesNo === 3 ? curQuesData.options(type) : curQuesData.options;
    // console.log(options)

        const backgroundImage = quesNo === 3 ? typeBgImg[type]: bgImg[quesNo-1];

    return (
        <div className='ques' style={{backgroundImage}}>
            <div className="top">
                TripTrouveAI
            </div>
            <h1 className='header'>Let us know your travel preferences!</h1>

            <div className="card">
                <h3>{curQuesData.ques}</h3>
                <div className="options-grid">
                    {options.map((option, index) => (
                        <button key={index} onClick={() => handleOption(option)} >{option}</button>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Question