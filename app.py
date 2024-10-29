from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Get input values
        frequency = float(request.form["frequency"])
        impedance = float(request.form["impedance"])
        z0 = 50  # Assuming a characteristic impedance of 50 ohms

        # Basic Calculations
        wavelength = 300 / frequency  # Wavelength in meters for given frequency in MHz
        swr = (impedance / z0) if impedance > z0 else (z0 / impedance)  # Simplified SWR calculation

        # Reflection Coefficient
        reflection_coefficient = (impedance - z0) / (impedance + z0)
        reflection_coefficient = round(reflection_coefficient, 2)  # rounding for display

        # Smith Chart Coordinates (normalized impedance)
        z_normalized = impedance / z0
        smith_real = round(z_normalized.real, 2)
        smith_imag = round(z_normalized.imag, 2)

        # Impedance matching by quarter-wave transformer
        transformer_impedance = (z0 * impedance) ** 0.5
        transformer_impedance = round(transformer_impedance, 2)
        
        # Compile the results
        result = (
            f"Calculated Wavelength: {wavelength:.2f} meters, "
            f"SWR: {swr:.2f}, "
            f"Reflection Coefficient: {reflection_coefficient}, "
            f"Smith Chart Coordinates (Real: {smith_real}, Imaginary: {smith_imag}), "
            f"Quarter-wave Transformer Impedance: {transformer_impedance} Ohms"
        )

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
