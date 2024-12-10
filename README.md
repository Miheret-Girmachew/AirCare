# AirCare

AirCare is a comprehensive air quality monitoring and alert system that enables users to track and receive real-time updates about air quality, smoke, and other harmful pollutants in their home or work environment. The system uses various sensors and communication modules to detect and send alerts via mobile apps, SMS, or cloud notifications.

## Features

- **Real-time air quality monitoring** for pollutants such as PM2.5, PM10, CO2, VOCs, and smoke.
- **Multi-home monitoring**: Track multiple locations simultaneously.
- **Customizable alerts**: Set threshold levels for pollutants, receive notifications via mobile app or SMS.
- **Integration with smart home systems** (optional): Control air purifiers, thermostats, etc., based on air quality.
- **Historical data and trends**: View data logs and trends for air quality over time.
- **User-friendly mobile app**: Provides push notifications and real-time data on your phone.

## Components

### 1. **Sensors & Microcontroller**
- **Air Quality Sensors**: Detects PM2.5, PM10, CO2, VOCs.
    - Example: DHT22, MQ-135, PMS5003
- **Smoke Detector**: Detects smoke levels.
    - Example: MQ-2, MQ-7
- **Microcontroller**: Arduino, ESP32, or Raspberry Pi to collect data from sensors and process it.

### 2. **Communication Modules**
- **Wi-Fi Module** (ESP8266, ESP32): Sends data to cloud servers and connects with mobile apps.
- **Bluetooth Module** (HC-05, ESP32 Bluetooth): Local communication with mobile apps.
- **SIM Module** (SIM800, SIM900): Sends SMS alerts or uses cellular data for cloud communication when Wi-Fi is unavailable.

### 3. **Cloud Server & Mobile App**
- **Cloud Server**: Firebase or AWS for data storage and alert management.
- **Mobile App**: Android/iOS app to monitor real-time data, receive notifications, and manage system settings.

## How It Works

1. **Data Collection**:
   - The air quality system collects data using sensors.
2. **Data Transmission**:
   - The microcontroller processes the data and sends it via Wi-Fi, Bluetooth, or SIM to the cloud server.
3. **Cloud Processing**:
   - Alerts are processed and sent to users via push notifications, SMS, or cloud-based dashboards.
4. **Alert Notifications**:
   - Users receive notifications based on predefined thresholds set for different pollutants (e.g., smoke detected, CO2 levels high).
5. **Multi-Home Monitoring**:
   - The app allows users to monitor and manage alerts from multiple homes or locations.

## Installation

### Requirements
- **Hardware**:
  - Microcontroller (Arduino, ESP32, Raspberry Pi)
  - Sensors (PM2.5, CO2, Smoke)
  - Communication modules (Wi-Fi, Bluetooth, SIM)
  
- **Software**:
  - Arduino IDE or ESP-IDF for programming microcontroller
  - Firebase or AWS for cloud server setup
  - Mobile app (Android/iOS)

### Setup Instructions

1. **Install Dependencies**:
   - Install the required libraries for sensors and communication modules.
   - Set up Firebase or AWS account for cloud communication.

2. **Microcontroller Setup**:
   - Flash the microcontroller with the appropriate code to read sensor data and send it to the cloud.

3. **App Setup**:
   - Download the mobile app from the app store (or use the provided app source code).
   - Configure the app to connect to your cloud server (e.g., Firebase).

4. **Cloud Server Setup**:
   - Set up Firebase Realtime Database or AWS IoT to store air quality data and handle alert notifications.

## Example Workflow

1. The system detects high smoke levels via the smoke sensor.
2. The microcontroller processes the data and sends it to the cloud via Wi-Fi.
3. The cloud server triggers a push notification to the user’s mobile app: “Smoke detected at Home 1. Please check immediately!”
4. The user can access detailed air quality data through the app, including historical trends and real-time measurements.

## App Features

- **Home Dashboard**: Monitor air quality at multiple homes.
- **Real-time Data Panel**: View live readings of air quality metrics (PM2.5, CO2, VOCs, etc.).
- **Alert History**: See historical alerts and trends for each home.
- **Custom Alert Settings**: Set thresholds for when to receive alerts.
- **Mobile Notifications**: Receive push notifications for critical alerts (e.g., smoke, high CO2).

## Contribution

If you'd like to contribute to the development of the AirCare system, feel free to fork this repository, submit issues, or create pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
