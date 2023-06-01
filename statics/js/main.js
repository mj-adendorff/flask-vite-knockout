import * as ko from "knockout";
import $ from "jquery";
import "../styles/style.css";

var MainView = {
  counter: ko.observable(0),
  time: ko.observable(""),
  updateCounter: function() {
    MainView.counter(MainView.counter() + 1);
    MainView.getTime();
  },
  getTime: function() {
    $.ajax({
      url: "/get-server-time",
      method: "GET",
      success: function(data) {
        MainView.time(data.time);
      }
    })
  },
}

ko.applyBindings(MainView, document.getElementById("app"));