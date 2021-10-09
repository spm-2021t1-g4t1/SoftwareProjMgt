//Imports
import { Link } from "react-router-dom"
import { FaHome , FaBookReader, FaComment, FaUser, FaCommentDots} from "react-icons/fa";

import { ProSidebar, Menu, MenuItem, SubMenu, SidebarContent ,SidebarFooter } from 'react-pro-sidebar';
import 'react-pro-sidebar/dist/css/styles.css';

// Modules
import React, { useState } from 'react'

const MainSidebar = () => {
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
                        <Link to="/" />
                    </MenuItem>
                    <SubMenu title="Course" icon={<FaBookReader />}>
                        <MenuItem>
                            Catalog
                            <Link to="/catalog" />
                        </MenuItem>
                        <MenuItem>
                            Course
                            <Link to="/course" />
                        </MenuItem>
                    </SubMenu>
                    <MenuItem icon={<FaComment />}>
                        Forum
                        <Link to="/" />
                    </MenuItem>
                    <MenuItem icon={<FaUser />}>
                        Account
                        <Link to="/account" />
                    </MenuItem>
                    <MenuItem icon={<FaCommentDots />}>
                        Mesages
                        <Link to="/" />
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

export default MainSidebar
