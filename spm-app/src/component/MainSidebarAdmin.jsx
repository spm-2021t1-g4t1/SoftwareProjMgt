//Imports
import { Link } from "react-router-dom"
import { FaHome , FaBookReader, FaComment, FaUser, FaCommentDots} from "react-icons/fa";
import { BsFillPeopleFill} from "react-icons/bs";


import { ProSidebar, Menu, MenuItem, SubMenu, SidebarContent ,SidebarFooter } from 'react-pro-sidebar';
import 'react-pro-sidebar/dist/css/styles.css';

// Modules
import React, { useState } from 'react'

const MainSidebarAdmin = () => {
    const [hovered, setHovered] = useState(false);
    const toggleHover = () => setHovered(!hovered);
    
    return (
        <ProSidebar className={hovered ? 'md': 'md collapsed'}
                onMouseEnter={toggleHover}
                onMouseLeave={toggleHover}>
            <SidebarContent>
                <Menu iconShape="circle">
                    <MenuItem icon={<FaHome />}>
                        Dashboard
                        <Link to="/Administrator/Dashboard" />
                    </MenuItem>
                    <SubMenu title="Course" icon={<FaBookReader />}>
                        <MenuItem>
                            Create Course
                            <Link to="/Administrator/Course/create" />
                        </MenuItem>
                        <MenuItem>
                            Avaliable Course
                            <Link to="/Administrator/Course/list" />
                        </MenuItem>
                    </SubMenu>
                    <SubMenu title="Engineers" icon={<BsFillPeopleFill />}>
                        <MenuItem>
                            Engineers list
                            <Link to="/Administrator/EngineerList" />
                        </MenuItem>
                        <MenuItem>
                            Approve self-enrollment
                            <Link to="/Administrator/Enrollment" />
                        </MenuItem>
                    </SubMenu>
                    <MenuItem icon={<FaComment />}>
                        Forum
                        <Link to="/Administrator/Forum" />
                    </MenuItem>
                    <MenuItem icon={<FaUser />}>
                        Account
                        <Link to="/Administrator/Account" />
                    </MenuItem>
                    <MenuItem icon={<FaCommentDots />}>
                        Mesages
                        <Link to="/Administrator/Message" />
                    </MenuItem>
                </Menu>
            </SidebarContent>
            <SidebarFooter>
                <div className = 'sidebar-btn-wrapper'>
                    Done by G4T1
                </div>
            </SidebarFooter>
        </ProSidebar>
    )
}

export default MainSidebarAdmin
