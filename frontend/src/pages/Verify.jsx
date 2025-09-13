import axios from 'axios';
import { useContext, useEffect } from 'react'
import { useNavigate, useSearchParams } from 'react-router-dom'
import { AppContext } from '../context/AppContext';
import { toast } from 'react-toastify';

const Verify = () => {
    const [searchParams] = useSearchParams() // Removed setSearchParams since it's not used
    const success = searchParams.get("success")
    const appointmentId = searchParams.get("appointmentId")
    const { backendUrl, token } = useContext(AppContext)
    const navigate = useNavigate()

    // Function to verify stripe payment
    const verifyStripe = async () => {
        try {
            const { data } = await axios.post(
                `${backendUrl}/api/user/verifyStripe`, 
                { success, appointmentId }, 
                { headers: { token } }
            )

            if (data.success) {
                toast.success(data.message)
            } else {
                toast.error(data.message)
            }
            navigate("/my-appointments")
        } catch (error) {
            toast.error(error.response?.data?.message || error.message)
            console.error(error)
            navigate("/my-appointments") // Navigate even on error
        }
    }

    useEffect(() => {
        if (token && appointmentId && success) { // Added proper conditional check
            verifyStripe()
        } else {
            // Handle missing parameters
            toast.error("Missing required parameters")
            navigate("/my-appointments")
        }
    }, [token, appointmentId, success, navigate]) // Added all dependencies

    return (
        <div className='min-h-[60vh] flex items-center justify-center'>
            <div className="w-20 h-20 border-4 border-gray-300 border-t-4 border-t-teal-700 rounded-full animate-spin"></div>
        </div>
    )
}

export default Verify