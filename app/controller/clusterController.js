import axios from "axios";

// predict cluster satu data user
export const predictCluster = async (req, res) => {
  try {
    const { umur, penghasilan } = req.body;
    if (!umur || !penghasilan) {
      res.json({
        message: "Gaggal Umur dan Penghasilan Harus di Isi",
      });
    } else {
      const response = await axios.post("http://127.0.0.1:5000/predict", {
        umur: umur,
        penghasilan: penghasilan,
      });

      // ubah response menjadi data json
      const result = response.data;

      res.status(200).json({
        message: "Success",
        data: result,
      });
    }
  } catch (error) {
    res.status(404).json({
      message: `API Not Found ${error}`,
    });
  }
};
