import './Card.css'
import pfp from './assets/julian.jpg'

function Card(){
    return(
        <>
            <div className="cards">
                <div className="card">
                    <img className="pfp" src={pfp} alt="profile picture"></img>
                    <h2>Julian Vrtiska</h2>
                    <p>IT Student and amateur video editor</p>
                </div>
            </div>
        </>
    );
}

export default Card