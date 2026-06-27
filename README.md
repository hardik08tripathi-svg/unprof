# unprof
#day 1 project
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

body {
    background: #f4f6f9;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 20px;
}

.profile-card {
    display: flex;
    max-width: 850px;
    width: 100%;
    background: #fff;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.profile-image {
    background: #eef2ff;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 30px;
    min-width: 250px;
}

.profile-image img {
    width: 170px;
    height: 170px;
    border-radius: 50%;
    object-fit: cover;
    border: 5px solid #4f46e5;
}

.profile-content {
    padding: 30px;
    flex: 1;
}

.profile-content h2 {
    color: #333;
    font-size: 28px;
}

.profile-content h4 {
    color: #4f46e5;
    margin: 8px 0;
}

.location {
    margin: 15px 0;
    color: #555;
}

.skills h3,
.about h3 {
    margin-bottom: 10px;
    color: #333;
}

.skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 20px;
}

.skill-tags span {
    background: #4f46e5;
    color: white;
    padding: 8px 14px;
    border-radius: 20px;
    font-size: 14px;
}

.about p {
    color: #666;
    line-height: 1.6;
    margin-bottom: 25px;
}

.contact-btn {
    background: #4f46e5;
    color: white;
    border: none;
    padding: 14px 28px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
    transition: 0.3s;
}

.contact-btn:hover {
    background: #3730a3;
}

/* Responsive Design */
@media (max-width: 768px) {
    .profile-card {
        flex-direction: column;
        text-align: center;
    }

    .profile-image {
        min-width: 100%;
        padding: 20px;
    }

    .skill-tags {
        justify-content: center;
    }

    .contact-btn {
        width: 100%;
    }
}
