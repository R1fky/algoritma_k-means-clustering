import axios from "axios";
export const predictCluster = async (req, res) => {
  try {
    const { umur, penghasilan } = req.body;
    if (!umur || !penghasilan) {
      res.json({
        message: "Gaggal Umur dan Penghasilan Harus di Isi",
      });
    } else {
      const response = await axios.post({
        umur: umur,
        penghasilan: penghasilan,
      });

      res.status(200).json({
        message: "Success",
        data: response,
      });
    }
  } catch (error) {
    res.status(404).json({
      message: `API Not Found ${error}`,
    });
  }
};
