import axios from "axios";

export default {
  getNeeds() {
    return axios
      .get("https://hackathon.spdns.eu/orpanage/need")
      .then(request => request.data);
  }
};
