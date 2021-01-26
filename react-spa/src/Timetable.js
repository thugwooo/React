import React, {Component} from "react";
import reviewPic from "./img/review.png";


class Timetable extends Component{
    render(){
        
        return(
            <div>
                <img src = {reviewPic} style alt="review"/>
            </div>
        );
    }
}
export default Timetable;