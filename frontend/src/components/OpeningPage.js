import React from "react";
import Title from "./Title";
import Auth from "./Auth";

function OpeningPage() {
    return (
        <div class="PageWrapper row">
            <div class="col-lg-6">
                <Title/>
            </div>
            <div class="col-lg-6">
                <Auth/>
            </div>
        </div>
    )
}

export default OpeningPage