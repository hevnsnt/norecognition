## **🗺️ Roadmap to v1.0**

### **v0.6: Persona** (in progress)**
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
    
### **v0.5: Anchor Code Health & Pattern Refinement**

**Theme:** Stabilize the fuzzer's core, enhance existing patterns, and improve digital robustness testing. This is a "quality of life" and "code health" release.

Codename: Anchor
This major release focuses on rock-solid stability for long-term fuzzer runs, accurate reporting, and the introduction of powerful new fuzzing capabilities to find deeper anomalies. We've tackled several critical performance and data integrity issues, particularly for Windows and CUDA users.

✨ New Features & Enhancements

* Expanded Fuzzing Power: The v0.5 branch kicks off with a new suite of patterns to increase fuzzer effectiveness. This includes banned_words, web attack strings, key feature blackout, rgb channel shift, and simulated optimized noise.
* Advanced Reporting: New 'Why/How' reports are now available, along with fuzzer strategy logging. This provides unprecedented insight into the fuzzer's decision-making process.
* Intelligent Resume: The --resume logic has been improved to automatically identify the previous state and confirm with the user before resuming a run.

🛡️ Stability & Data Integrity Fixes

* Long-Term Run Stability: Two critical performance bottlenecks that caused the main fuzzer thread to stall have been resolved, ensuring stable, long-term operation.
* Crash-Proof State Saving: The end-of-epoch state saving is now atomic and crash-proof. The logic has been re-ordered and bugs related to intermittent file locks (especially on Windows) have been fixed, guaranteeing that the fuzzer_state.json file is saved reliably.

Core Bug Fixes:

 * Resolved critical data logging and worker crash bugs that were causing instability.
 * Fixed fundamental issues in worker arguments and pattern logic.

📊 Reporting & Metric Accuracy

* Critical Plotting Fix: Fixed a critical bug in plot_reports.py where statistics were incorrectly grouped by the full recipe string. Reports now correctly "explode" recipes to aggregate statistics for individual patterns (e.g., 'vortex') independently, ensuring accurate and statistically valid one-pager plots.

💻 Platform & Hardware Fixes (Windows/CUDA/MLX)

* Windows Compatibility: Squashed several "windows UTF-8 bugs" and resolved issues with os.rename() file locks, greatly improving reliability on Windows systems.

GPU Backend Fixes:

 * Fixed several CUDA GPU bugs that affected execution on various NVIDIA setups.
 * Addressed a crash caused by hardware acceleration code in patterns.py that was using incorrect syntax for the MLX backend.

🐛 Pattern-Specific Bug Fixes

* Digital Robustness Fix: Fixed a bug where models were being evaluated against the original image instead of the augmented image during digital robustness checks.
* Blurring Fix: Resolved bugs in apply_selective_blur and apply_landmark_noise where the functions were incorrectly blurring a blank canvas instead of the original_image.

🏗️ Refactoring & Code Health

* Initial Core Refactoring: The monolithic fuzzer class has been refactored into more logical and maintainable modules: state_manager.py, tui_manager.py, and worker_manager.py.

---

### **v0.4: TUI Implementation**
Code name: Vector
This commit introduces v0.4, a major refactor focused on TUI performance, enhanced anomaly detection, and worker robustness. It replaces the v0.3 Live display strategy with a high-performance, persistent layout, and introduces a more granular, research-focused anomaly detection system.

This commit also includes critical fixes to resolve initialization crashes and logic errors present in the initial v0.4 branch.

🚀 TUI 2.0 & Performance

* The TUI has been completely rewritten for performance and features.
* Persistent Layout: The Live display no longer rebuilds the entire layout on every refresh. A persistent rich.Layout is built once (_build_initial_layout), and its panels (stats_panel, log_panel, etc.) are updated in-place by swapping their .renderable content (_update_layout_content).
* Massive Performance Gain: This change dramatically reduces CPU usage, eliminates TUI flicker, and allows for much higher refresh rates.
* ✨ New Anomaly Preview Panel: A new panel has been added to the TUI. When a FACE_ENSEMBLE anomaly is found, its saved image is loaded, resized via rich-pixels, and displayed directly in the terminal for real-time visual feedback.
* Improved History: Epoch history is now cleanly displayed below the progress bar and persists across fuzzer restarts.

🔬 Anomaly Detection & Evolutionary Logic

* The anomaly detection and evolutionary logic has been made more granular and effective for research.
* New Anomaly Types: The simple FACE_LOW_CONF and PERSON anomalies from v0.3 have been expanded. We now explicitly detect and log:
    FACE_ENSEMBLE: (High Priority) Primary face lost by all models.
    FACE_LOST: (Standard Priority) Primary face lost by any model.
    FACE_INCREASE: More faces detected than baseline (hallucination).
    PERSON_LOST: Person (from YOLO) lost.
    PERSON_INCREASE: More persons detected than baseline.

* Targeted Artifact Saving: The _save_anomaly_artifacts function has been modified to only save images, patterns, and recipes for the most critical FACE_ENSEMBLE anomalies. This prevents anomaly/ directories from being flooded with lower-priority findings.
* Evolutionary Queue Fix: The priority_tests list (used for the evolutionary algorithm) is now correctly populated. All anomaly types (standard and high-priority) are added to the queue to be mutated, ensuring a diverse genetic pool for the fuzzer.

🐛 Critical Fixes

This commit resolves several critical crashes and logic bugs:

* Fixed Fuzzer Crash: Fixed an AttributeError on startup by correctly initializing self.log = main_process_logger in Fuzzer.__init__. This fixes the "broken" main error logging.
* Fixed Progress Crash: Fixed a TypeError by removing the invalid console=console argument from the rich.Progress constructor. This resolves the TUI failing to start.
* Fixed Status Bar: The console.status() calls in establish_baselines were not "broken"; they were simply never reached due to the Fuzzer crash. This is now fixed.
* Fixed Anomaly Preview: The preview panel was not "broken"; it was also a victim of the TUI not starting. This is now fixed and functional.

👷 Worker & Architecture Improvements

* Robust Worker Classes: AnalysisWorker and BaselineWorker are now proper classes that encapsulate their own models and state.
* Isolated Worker Logging: All worker processes now use rich.logging to log their full setup and runtime output to individual files in Output/worker_logs/. This is a massive improvement for debugging multiprocessing issues.
* Robust Model Init: initialize_model no longer calls exit() on failure. It now returns None and logs the error, allowing the worker to handle the failure gracefully.
* Crash Handling: Worker pool functions (run_analysis_worker, baseline_worker) now have top-level try...except blocks to catch and return unexpected crashes as serializable error dictionaries, preventing the main fuzzer from hanging.

---

### **v0.3: TUI Implementation**
Version 0.3 – Rich TUI Integration & Reporting enhancements
Code Name: Svelte

    Integrated the Rich library to introduce an interactive terminal user interface (TUI).
    Added real-time progress panels, visual summaries, and better runtime feedback.
    Improved code readability and logging consistency.
    Drastically improved reporting output, providing clearer test summaries and anomaly visibility.
    Completed a round of cleanup and optimizations before branching to v0.4.
    Updated folder structure

---

### **v0.2: Refactored into object-oriented components**
Version 0.2 – Refactored into object-oriented components for easier testing and scaling
Code Name: Classy

    Added the classy_fuzz.py module, marking a major structural shift in the project.
    Refactored core functionality into object-oriented components for easier testing and scaling.
    Improved the fuzzing logic and data handling pipelines.
    Enhanced reliability and debugging output across the system.
    Significant additions and speed improvements for all pattern generators.
    Enhanced GPU capabilities and efficiencies

---
### Version v0.1 – Initial Development (Proof of concept release)
Code Name: Seed (The concept planted that everything else grew from)

    Established the foundation of the codebase.
    Implemented early structure, core modules, and baseline functionality.
    Developed initial logic for core processing routines and file handling.
    Focused on achieving a stable proof of concept for early fuzzing and testing.
    Proof of concept

---
---
# Future Roadmap

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

