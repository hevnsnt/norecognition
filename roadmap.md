## **🗺️ Roadmap to v1.0**

### **v0.5: Code Health & Pattern Refinement**

**Theme:** Stabilize the fuzzer's core, enhance existing patterns, and improve digital robustness testing. This is a "quality of life" and "code health" release.

* **Fuzzer Core Refinement:**  
  * Address the technical debt mentioned in the README's proposals.  
  * ~~**Refactor the monolithic `Fuzz` class** in `classy_fuzz.py` into more logical, maintainable modules (e.g., `TUI_Manager`, `StateManager`, `WorkerPool_Manager`).~~ [complete]  
  * **Improve the TUI `Anomaly Preview` resolution** (as noted in the README) to make real-time analysis more useful.  
  * ~~**Strengthen the `--resume` logic** to be more robust.~~  [complete]
* **Surgical Pattern Expansion:**  
  * Refine and expand the existing pattern library (`patterns.py`) with a focus on **landmark-aware "surgical" attacks**.  
  * Create more variants of `dazzle_camouflage` and `adversarial_patch` that specifically target different feature combinations (e.g., eye-to-nose, brow-to-cheek).  
* **Digital Robustness Testing:**  
  * Implement a **digital augmentation pre-processor**.  
  * Before analysis, automatically apply minor, randomized transformations to the generated image (e.g., slight rotation `[-5, 5]` degrees, scaling `[0.9, 1.1]`, brightness/contrast jitter). This begins testing pattern robustness in "real-world" (digital) conditions.

---

### **v0.6: The "Persona" Release (Controlled Testing)**

**Theme:** Move from random synthetic data to a fixed, high-quality, and diverse dataset. This establishes the **scientific baseline** for all future tests.

* **Persona Dataset Integration:**  
  * Integrate the 6 new "Persona" images (Gary, Barry, Larry, Carrie, Mary, Sherry) as the **primary input targets**.  
  * Ensure these images are high-resolution and feature consistent lighting and poses (e.g., frontal, 3/4 profile) to create a research-grade testbed.  
* **Baseline Regeneration:**  
  * **Purge all old baseline data** generated from "This Person Does Not Exist."  
  * Run the baseline process on the 6 new personas to generate and save new, high-quality landmark and detection data. This becomes the "ground truth."  
* **Report Re-tooling:**  
  * Update `plot_reports.py` to generate new reports specifically focused on this 6-persona set.  
  * The "Target Image Vulnerability" report (`1_2_target_vulnerability_full_history.png`) now becomes a core "Persona Leaderboard," showing which persona is most/least vulnerable.

---

### **v0.7: Introducing Facial Recognition (1:N Matching)**

**Theme:** Graduate the fuzzer from *detection* failure to *recognition* failure. This addresses the core goal of defeating "facial recognition," not just "person detection."

* **1:N Matching Pipeline:**  
  * Implement the **Facial Recognition Matching Pipeline** as proposed in the README.  
  * Integrate a model like **ArcFace** to generate feature embeddings for detected faces.  
* **Persona Identity Database:**  
  * Create a "gallery" database containing the "ground truth" facial embeddings for the 6 personas.  
  * The fuzzer will now match detected faces *against* this gallery.  
* **New Anomaly Types:**  
  * Upgrade the fuzzer's analysis logic (`_check_for_anomalies` in `classy_fuzz.py`) to understand new failure states:  
    1. **`RECOGNITION_FAILURE`**: A face is detected, but its embedding does *not* match the correct persona in the gallery (below a confidence threshold).  
    2. **`MISIDENTIFICATION`**: A face is detected, and its embedding *incorrectly* matches the *wrong* persona in the gallery.

---

### **v0.8: Intelligent Evolution & Deeper Analysis**

**Theme:** Refine the new recognition testing, make the genetic algorithm "smarter," and expand the model ensemble.

* **Goal-Oriented Genetic Algorithm:**  
  * Upgrade the genetic algorithm to be **goal-oriented**.  
  * Allow the user to specify an evolutionary goal (e.g., `fuzz-for: detection-failure` vs. `fuzz-for: misidentification`). The fuzzer will then prioritize "parent" patterns that successfully caused that specific anomaly type.  
* **New Recognition Reports:**  
  * Expand `plot_reports.py` to visualize 1:N matching failures.  
  * Key reports to add:  
    * **Recognition Failure Rate %** (by pattern, by persona).  
    * **Confusion Matrix** (which persona was most often mistaken for whom?).  
* **Model Ensemble Expansion (Open Source):**  
  * Begin implementing the "Distant future" roadmap item.  
  * Add other common open-source *detectors* (e.g., **MTCNN**, **RetinaFace**) to the *baseline* analysis. A pattern is now considered *more robust* if it fools InsightFace *and* RetinaFace.

---

### **v0.9: The "Real-World" & Cloud Audit Release**

**Theme:** Bridge the gap between digital simulation and physical reality. Test patterns against the true "state-of-the-art" (closed-source cloud APIs).

* **Physical Test Harness (P-Harness):**  
  * Develop a new "Physical Test Harness" script (`p_harness.py`).  
  * This script will use a webcam (`cv2.VideoCapture`) to run the *full detection and recognition pipeline* (from v0.7-v0.8) in real-time on a physically printed fabric.  
  * This provides the crucial **Digital-to-Physical (D2P)** feedback loop.  
* **Cloud API Auditing:**  
  * Implement the "Distant future" roadmap item for auditing cloud APIs.  
  * Create a module that (on a rate-limited, user-opt-in basis) sends high-priority anomaly images to endpoints like **AWS Rekognition** and **Azure Face API**.  
  * A "High Priority Anomaly" is now one that fools *both* local models *and* a cloud API.  
* **Digital-to-Physical (D2P) Correlation Report:**  
  * Create a new report that correlates digital success rates with physical test results. This is the most important report for the project's mission.  
  * It answers: "Which patterns (e.g., `fractal_noise`) are highly effective in *both* digital and physical tests?"

---

### **v1.0: "Research-Ready" Release**

**Theme:** Package the entire project as a stable, reproducible, and well-documented research tool.

* **Code Stability & Documentation:**  
  * A final, major refactoring pass to clean up all code. Split `classy_fuzz.py` into its final modular form.  
  * Implement full code documentation (docstrings, type hinting) and write a "Getting Started" guide so other researchers can *exactly* reproduce your results.  
* **Final "Golden Set" Epoch:**  
  * Run a final, large-scale (e.g., 100M+ tests) fuzzing campaign using the full v0.9 ensemble (local models, cloud APIs, and physical harness validation).  
  * Identify the **Top 3-5 "Golden" Patterns** that are verifiably robust against the widest range of models.  
* **Comprehensive Research Report:**  
  * Finalize `plot_reports.py` to generate a single, comprehensive PDF or HTML "Research Report" that summarizes the project's findings, including:  
    * Detection vs. Recognition success rates.  
    * Digital vs. Physical (D2P) correlation.  
    * Cloud API audit results.  
    * The v1.0 "Golden" patterns and their print-ready files.

