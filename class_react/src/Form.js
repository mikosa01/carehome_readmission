import { useState } from "react";
import './Form.css';

function Form() {
    const[form, setForm] = useState({
        gender: '',
        mental_health_issues: '',
        polypharmacy: '',
        nutritional_status: '',
        follow_up_completed: '',
        care_plan_adherence: '',
        staffing_level: '',
        family_involvement: '',
        hospital_acquired_infections: '',
        discharge_timing: '',
        chronic_conditions: '',
        previous_hospitalizations: '',
        age: ''
    }); 

    const [loading, setLoading] = useState(false)
    const [result, setResult] = useState(' ')
    const handlerSubmit = (event) => {
        event.preventDefault(); 
        const form_data = new FormData();
        form_data.append('1', form.gender);
        form_data.append('2', form.mental_health_issues);
        form_data.append('3', form.polypharmacy);
        form_data.append('4', form.nutritional_status);
        form_data.append('5', form.follow_up_completed);
        form_data.append('6', form.care_plan_adherence);
        form_data.append('7', form.staffing_level);
        form_data.append('8', form.family_involvement);
        form_data.append('9', form.hospital_acquired_infections);
        form_data.append('10', form.discharge_timing); 
        form_data.append('11', form.chronic_conditions);
        form_data.append('12', form.previous_hospitalizations);
        form_data.append('13', form.age);

        setLoading(true);

        fetch('https://care-home-backend-d893d8a8a937.herokuapp.com/predict',{
            method: 'POST',
            body: form_data
        })
            .then(response => response.text())
            .then(html => {
                setResult(html);
                setLoading(true)
        })
    };

    const onChange = (event) => {
            const name = event.target.name
            const value = event.target.value 
            setForm({...form, [name] :[value]});
                }
    
    const handlerClear = () => {
        setForm({
            gender: '',
            mental_health_issues: '',
            polypharmacy: '',
            nutritional_status: '',
            follow_up_completed: '',
            care_plan_adherence: '',
            staffing_level: '',
            family_involvement: '',
            hospital_acquired_infections: '',
            discharge_timing: '',
            chronic_conditions: '',
            previous_hospitalizations: '',
            age: ''
        });
        setResult('')
    }

    return(

        <div>
            {/* Note about the project aim, goal, and disclaimer */}
            <div className="project-note">
                <h3>Aim and Goal of the Project</h3>
                <p>
                    The primary aim of this project is to predict the likelihood of a care home readmission based on a variety of health and social factors. By analyzing historical health data, we aim to assist care home administrators and healthcare providers in making informed decisions to prevent unnecessary readmissions.
                </p>
            </div>
            <form onSubmit={handlerSubmit}>
                <h>Care Home Readmssion</h>
                <p>Care home Readmssion prediction probabililities</p>
                <select id="gender" name="gender" value={form.gender} onChange={onChange} required>
                <option value="" disabled selected>Select Gender</option>
                <option value="0">Female</option>
                <option value="1">Male</option>
                </select>
                <select id="mental_health_issues" name="mental_health_issues" value={form.mental_health_issues} onChange={onChange} required>
                <option value="" disabled selected>Do you have any mental health conditions?</option>
                <option value="0">No</option>
                <option value="1">Yes</option>
                </select>
                <select id='polypharmacy' name='polypharmacy' value={form.polypharmacy} onChange={onChange} required>
                <option value="" disabled selected>Do you have multiple pharmacy?</option>
                <option value="0">No</option>
                <option value="1">Yes</option>
                </select>
                <select id='nutritional_status' name='nutritional_status' value={form.nutritional_status} onChange={onChange} required>
                <option value="" disabled selected>What is your current nutritional status? </option>
                <option value="0">Good</option>
                <option value="1">Moderate</option>
                <option value="2">Poor</option>
                </select>
                <select id='follow_up_completed' name='follow_up_completed' value={form.follow_up_completed} onChange={onChange} required>
                <option value="" disabled selected>Have you completed the follow-up? </option>
                <option value="0">Yes</option>
                <option value="1">No</option>
                </select>
                <select id='care_plan_adherence' name='care_plan_adherence' value={form.care_plan_adherence} onChange={onChange} required>
                <option value="" disabled selected>How would you describe your adherence to your care plan? </option>
                <option value="0">High</option>
                <option value="1">Medium</option>
                <option value="2">Low</option>
                </select>
                <select id='staffing_level' name='staffing_level' value={form.staffing_level} onChange={onChange} required>
                <option value="" disabled selected>What was the staffing level? </option>
                <option value="0">Adequate</option>
                <option value="1">Inadequate</option>
                </select>
                <select id='family_involvement' name='family_involvement' value={form.family_involvement} onChange={onChange} required>
                <option value="" disabled selected>Is your family involved in your care?</option>
                <option value="0">Active</option>
                <option value="1">Moderate</option>
                <option value="2">Inactive</option>
                </select>
                <select id='hospital_acquired_infections' name='hospital_acquired_infections' value={form.hospital_acquired_infections} onChange={onChange} required>
                <option value="" disabled selected>Have you experienced any hospital-acquired infections (HAIs)? </option>
                <option value="0">Yes</option>
                <option value="1">No</option>
                </select>
                <select id='discharge_timing' name='discharge_timing' value={form.discharge_timing} onChange={onChange} required>
                <option value="" disabled selected>When was your discharge time? </option>
                <option value="0">Weekday</option>
                <option value="1">Weekend</option>
                </select>
                <input type='number' name= 'chronic_conditions' value = {form.chronic_conditions} onChange={onChange} placeholder="Number of Chronic Conditions Suffered" required/>
                <input type='number' name= 'previous_hospitalizations' value = {form.previous_hospitalizations} onChange={onChange} placeholder="How many times have you been hospitalized for medical reasons?" required/>
                <input type='number' name= 'age' value = {form.age} onChange={onChange} placeholder=" What is your age?" required/>
                <button type="submit" disable={loading}> {loading? 'Predicting result ....': 'Submit Form'} </button>
                {result && <span onClick={handlerClear}> Clear Button</span>}
                {result && <div dangerouslySetInnerHTML = {{__html: result}} className='result'/>}
            </form>
            < div className="Disclaimer">
            
            <h3>Disclaimer</h3>
            
            <p className="moving-text">
                This tool is intended for informational purposes only. The predictions made by the model
                are based on the provided data and should not be considered as medical advice. Always
                consult a healthcare professional for accurate diagnosis and treatment options. The
                developers are not responsible for any decisions made based on the predictions provided by
                this form.
            </p>
            
            </div>
        </div>
    )

    

    

}

export default Form;