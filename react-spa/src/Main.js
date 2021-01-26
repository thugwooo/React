import React, {Component} from "react";
import {Route, NavLink, HashRouter} from "react-router-dom";
import Profile from "./Profile";
import Notice from "./Notice";
import Classes from "./Classes";
import TimeTable from "./Timetable";
import VideoLink from "./VideoLink";

class Main extends Component{
    render(){
        return(
            <HashRouter>
                <div>
                    <h1>대치동 다영쌤</h1>
                    <ul className ="header">
                        <li><NavLink exact to="/">프로필</NavLink></li>
                        <li><NavLink to="/1">수업구성</NavLink></li>
                        <li><NavLink to="/2">공지사항</NavLink></li>
                        <li><NavLink to="/3">시간표</NavLink></li>
                        <li><NavLink to="/4">수업영상</NavLink></li>
                    </ul>
                    <div className="content">
                        <Route exact path="/" component={Profile}/>
                        <Route path="/1" component={Classes}/>
                        <Route path="/2" component={Notice}/>
                        <Route path="/3" component={TimeTable}/>
                        <Route path="/4" component={VideoLink}/>
                    </div>
                </div>
            </HashRouter>
        );
    }
}

export default Main;