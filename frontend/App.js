import React, { useEffect, useState } from "react";
import { View, Text, FlatList } from "react-native";
import MapView, { Marker } from "react-native-maps";

const App = () => {
    const [buses, setBuses] = useState([]);

    useEffect(() => {
        fetch("http://localhost:5000/buses")
            .then(response => response.json())
            .then(data => setBuses(data));
    }, []);

    return (
        <View style={{ flex: 1 }}>
            <MapView style={{ flex: 1 }} initialRegion={{
                latitude: 40.730610,
                longitude: -73.935242,
                latitudeDelta: 0.1,
                longitudeDelta: 0.1,
            }}>
                {buses.map((bus) => (
                    <Marker
                        key={bus.id}
                        coordinate={{ latitude: bus.latitude, longitude: bus.longitude }}
                        title={`Route: ${bus.route}`}
                        description={`Arrival Time: ${bus.arrival_time}`}
                    />
                ))}
            </MapView>
        </View>
    );
};

export default App;
