import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Checkbox } from "@/components/ui/checkbox";
import { useState } from "react";

export default function MobilePreCheck() {
  const [step, setStep] = useState(1);

  return (
    <div className="max-w-md mx-auto p-6 space-y-6">
      {step === 1 && (
        <Card>
          <CardContent className="space-y-4">
            <h2 className="text-xl font-bold">Welcome to QuickER Pre-Check</h2>
            <p className="text-gray-500">Skip the paperwork. Save time.</p>
            <Button onClick={() => setStep(2)}>Start Pre-Check</Button>
          </CardContent>
        </Card>
      )}

      {step === 2 && (
        <Card>
          <CardContent className="space-y-4">
            <h2 className="text-xl font-bold">Patient Info</h2>
            <Input placeholder="Full Name" />
            <Input type="date" placeholder="Date of Birth" />
            <Input placeholder="Email" />
            <Input placeholder="Phone" />
            <Button onClick={() => setStep(3)}>Next</Button>
          </CardContent>
        </Card>
      )}

      {step === 3 && (
        <Card>
          <CardContent className="space-y-4">
            <h2 className="text-xl font-bold">Symptoms & Reason</h2>
            <Input placeholder="Describe your symptoms" />
            <Button onClick={() => setStep(4)}>Next</Button>
          </CardContent>
        </Card>
      )}

      {step === 4 && (
        <Card>
          <CardContent className="space-y-4">
            <h2 className="text-xl font-bold">Insurance & ID</h2>
            <Input type="file" />
            <Input type="file" />
            <Button onClick={() => setStep(5)}>Next</Button>
          </CardContent>
        </Card>
      )}

      {step === 5 && (
        <Card>
          <CardContent className="space-y-4">
            <h2 className="text-xl font-bold">Consent & Submit</h2>
            <div className="flex items-center space-x-2">
              <Checkbox id="consent1" />
              <label htmlFor="consent1">Consent to treatment</label>
            </div>
            <div className="flex items-center space-x-2">
              <Checkbox id="consent2" />
              <label htmlFor="consent2">Agree to privacy policy</label>
            </div>
            <Button onClick={() => setStep(6)}>Submit</Button>
          </CardContent>
        </Card>
      )}

      {step === 6 && (
        <Card>
          <CardContent className="space-y-4">
            <h2 className="text-xl font-bold">You’re checked in!</h2>
            <p>Head to the ER front desk when you arrive.</p>
            <p>Estimated wait time: 15 mins</p>
            <Button variant="outline">Get Directions</Button>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
