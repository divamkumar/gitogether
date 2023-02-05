import React from "react";
import Title from "./Title";
import Auth from "./Auth";

function OpeningPage() {
    return (
        <div className="PageWrapper row">
            <div className="col-lg-6">
                <Title/>
            </div>
            <div className="col-lg-6">
                <Auth/>
            </div>
        </div>
    )
}

export default OpeningPage