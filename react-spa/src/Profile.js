import React, {Component} from "react";
import profilepic from "./img/profile.png";
import youtubelogo from "./img/BLOGYOUTUBELOGO2.jpg"
import naverimg from "./img/naverimg.png"
class Profile extends Component{
    render(){
        return(
            <div>
                <img src = {profilepic} alt="profile"/>
                <h2>약력</h2>
                <ul>
                    <li>서강대 수학과 졸업</li>
                    <li>현 시대인재</li>
                    <li>현 콴다 “대치동다영쌤”</li>
                    <li>전 대치 새움학원</li>
                    <li>전 대치 하이매쓰</li>
                    <li>전 스카이입시교육 내신기출 인강</li>
                    <li>전 코드엠수학 검토위원</li>
                </ul>
                <h2>링크로 이동</h2>
                <ul>
                    <a href="https://blog.naver.com/beautemps_"><img src={naverimg} alt="naverimg"/></a>
                    <a href="https://www.youtube.com/channel/UCQly8d11ZwPiyyDBxHM4Iwg"><img src= {youtubelogo} alt="yotubelogo"/></a>
                </ul>
            </div>
        );
    }
}

export default Profile;