# **Web-Based Sentiment Analysis Dashboard for Participatory Urban Planning**

![Screenshot 2025-01-18 171157](https://github.com/user-attachments/assets/5f00c5aa-06fb-4d5c-99e2-4df0c69ef0ff)

## **Description**

The **Sentiment Analysis Dashboard** is a web application designed to collect, analyze, and visualize sentiment from user feedback, aiding participatory urban planning processes. It leverages advanced text analysis using AWS APIs and provides an intuitive interface for both administrators and users. The dashboard features an interactive map for geographic feedback visualization and insightful charts to showcase sentiment trends.

---

## **Features**

- **Interactive Map**  
  Powered by **Mapbox GL JS**, the map allows users to submit location-based feedback and view geographically pinned sentiments.  
- **Sentiment Analysis**  
  Utilizes **AWS Comprehend** to analyze user-submitted text for **positive**, **negative**, and **neutral** sentiments.  
- **Data Visualization**  
  Interactive charts created with **Chart.js** display real-time sentiment distribution, trends, and feedback timelines.  
- **User-Friendly Interface**  
  Built with **vanilla JavaScript** and styled using modern **CSS**, ensuring seamless navigation and functionality.

---

## **Technologies Used**

- **Flask**: Backend framework for handling API requests and routing.  
- **AWS Comprehend**: For powerful sentiment analysis.  
- **Mapbox GL JS**: To enable dynamic map-based visualization.  
- **Chart.js**: For creating real-time, interactive sentiment charts.  
- **Vanilla JavaScript and CSS**: Lightweight client-side scripting and styling.

---

## **Prerequisites**

1. **Python and Flask Installed**  
   Ensure Python and Flask are installed on your system.  
2. **AWS Comprehend Access**  
   An AWS account with Comprehend enabled. Configure AWS credentials locally.  
3. **Mapbox Token**  
   Create a Mapbox account and obtain your API token for map integration.  

---

## **Setup Instructions**

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/mohammadvhb/Sentiment-Analysis-Map.git  
   cd Sentiment-Analysis-Map
   ```
2. **Install Dependencies**  
   Install Python dependencies from the requirements file:  
   ```bash
   pip install -r requirements.txt  
   ```
3. **Configure AWS**  
   Set up AWS credentials using the AWS CLI or environment variables. Replace placeholders in the application code with your credentials.  
4. **Set Up Mapbox**  
   Replace the `mapboxgl.accessToken` in `index.html` with your Mapbox access token.  
5. **Start the Flask Application**  
   Launch the server:  
   ```bash
   python app.py  
   ```
6. **Access the Application**  
   Open your browser and navigate to:  
   ```
   http://localhost:5000  
   ```

---

## **Usage**

1. **Submit Feedback**  
   Click on the interactive map to open a form, enter your feedback, and submit.  
2. **View Sentiments**  
   Sentiment markers appear on the map. Charts and statistics update in real-time based on user feedback.  
3. **Analyze Trends**  
   Use the visualizations to identify sentiment trends and insights for urban planning strategies.

---

## **Contact**

Feel free to reach out for inquiries, collaborations, or feedback:  
- **Email**: [m.vahidiborji@gmail.com](mailto:m.vahidiborji@gmail.com)  
- **Website**: [mohammadvahidi.com](https://mohammadvahidi.com)  
- **LinkedIn**: [linkedin.com/in/mohammadvh](https://linkedin.com/in/mohammadvh)

