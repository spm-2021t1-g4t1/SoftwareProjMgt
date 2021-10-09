import React from 'react'
import { Link } from "react-router-dom"
import { ProSidebar, Menu, MenuItem, SubMenu, SidebarContent } from 'react-pro-sidebar';
import { FaBookReader} from "react-icons/fa";


const CourseSidebar = () => {

    return (

        <ProSidebar className = 'classSideBar'>
            <SidebarContent>
            <Menu iconShape="circle">
                <SubMenu title="Class Sidebar" icon={<FaBookReader />}>
                    <MenuItem>
                        Overview
                        <Link to="./overview" />
                    </MenuItem>
                    <MenuItem>
                        Curriculum
                        <Link to="./curriculum" />
                    </MenuItem>
                    <MenuItem>
                        Course Forum
                        <Link to="./forum" />
                    </MenuItem>
                    <MenuItem>
                        Take Quiz
                        <Link to="./quiz" />
                    </MenuItem>
                </SubMenu>
            </Menu>
            </SidebarContent>
        </ProSidebar>
    )
}

export default CourseSidebar
