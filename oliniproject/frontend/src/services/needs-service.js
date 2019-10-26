import axios from "axios";

export default {
  getNeeds() {
    return axios
      .get("http://10.4.169.200:8080/orpanage/need")
      .then(request => request.data);
  }
};
