import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Controls.Material 2.0
import QtQuick.Controls.Material 2.3

Rectangle {
    width:400;height:400;
    color: Material.color(Material.Red)
    Button {
        text: qsTr("Button")
        highlighted: true
        Material.background: Material.Teal
    }
    Button {
        text: "A"
    }

    Button {
        text: "B"
    }

    Button {
        text: "C"
    }
    
}
